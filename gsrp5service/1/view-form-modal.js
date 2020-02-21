import {csvJSON,csvUpload} from '../../js/utils.js'
import {on_new_many2one,on_detail_many2one,on_find_many2one,on_find_many2one_update,on_new_related,on_detail_related,on_find_related,on_find_related_update,readonly,required,m2o_new,m2o_put,related_new,related_put,on_add_models,on_update_models,on_remove_models,visible,selFrom,selFromForm,cache,on_cache,m2o_cache,on_m2o_cache,related_cache,on_related_cache,send} from '../../mixins/nf-1.js'
import Vue from 'vue'
import uuidv4 from 'uuid/v4'

export default {
	name:'gsrp5-form-view-modal',
	//props: {'metas':Object,'model':String,'path':{'default':null},'modal':{'default':false}},
	data: () => ({
	  swipeDirection: 'None',
	  metas:null,
	  meta: null,
	  views:null,
	  mode: 'new',
	  model:null,
	  path:null,
	  modal:true,
	  root:null,
	  name: null,
	  obj: null,
	  rel:null,
	  idx: -1,
	  guid:null,
	  oids:null, 
	  active: null,
	  dialog:true,
	  valid: false,
	  rules: {},
	  view:{},
	  selected:[],
	  menu:{},
	  fields: [],
	  formfields: [],
	  o2mfields: [],
	  template: null,
	  selectionFrom: {},
	  selectionFromForm: {},
      c: {},
      d: {},
      m: {},
      item: {},
    }),
    watch: {
      dialog (val) {
        val || this.close()
      },
   importedData: {
      handler() {
        this.checkData();
      },
      deep: true
    }
    },
    mixins: [{methods:{on_new_many2one:on_new_many2one,on_detail_many2one:on_detail_many2one,on_find_many2one:on_find_many2one,on_find_many2one_update:on_find_many2one_update,on_new_related:on_new_related,on_detail_related:on_detail_related,on_find_related:on_find_related,on_find_related_update:on_find_related_update,readonly:readonly,required:required,m2o_new:m2o_new,m2o_put:m2o_put,related_new:related_new,related_put:related_put,on_add_models:on_add_models,on_update_models:on_update_models,on_remove_models:on_remove_models,visible:visible,cache:cache,on_cache:on_cache,m2o_cache:m2o_cache,on_m2o_cache:on_m2o_cache,related_cache:related_cache,on_related_cache:on_related_cache,send:send}}],
    methods: {
        swipe (direction) {
          this.swipeDirection = direction
        },
        validate () {
	       if (this.$refs.form.validate()) {
	         this.snackbar = true;
	       }
	        else {
			this.snackbar = false;
			   }
	     },
	     clear () {
			this.d = {};
			this.c = {};
			this.m = {};
			this.send('onInitialize',['_cache','initialize',this.guid,{'model':this.model,'view':'form'}]);
		 },
		on_selected (s){
			this.selected = s;
			},
		_fieldsBuild(model,fields,sm){
			let field,k,obj;
			for(let i = 0;i < fields.length;i++){
				field = fields[i];
				//console.log(model,field);
				switch(this.metas[model].meta.columns[field].type){
					case 'one2many':
						 obj = this.metas[model].meta.columns[field].obj;
						 if (!(obj in sm)) continue;
						 if (obj in this.metas){
							 if (this.o2mfields.indexOf(field) == -1){
								k = {};
								//this.o2mfields.push(field); 
								if (field == this.metas[model].meta.names.childs_id) k[field] = Object.keys(this.metas[obj].views.list.columns);
								else k[field] = this._fieldsBuild(obj,Object.keys(this.metas[obj].views.list.columns),this.metas[obj].meta.schema);
								fields[i] = k;
								}
							}
						break;					
					case 'many2many':
						 k = {};
						 //this.m2mfields.push(field); 
						 obj = this.metas[model].meta.columns[field].obj;
						 k[field] = Object.keys(this.metas[obj].views.m2mlist.columns);
						 fields[i] = k;
						break;
					case 'selection':
						this.selectionFromForm[field] = selFromForm(this.metas[model].meta.columns[field].selections);
						this.selectionFrom[field] = selFrom(this.metas[model].meta.columns[field].selections);
						break;
					case 'referenced':
						let r = this.metas[model].meta.columns[field].ref.split('.')
						obj = this.metas[model].meta.columns[r[0]].obj;
						//fields[i] = this._fieldBuild(obj,[r[1]],sm);
							break;
					}
			}
			return fields;
			},
        previewImage: function(event) {
            // Reference to the DOM input element
            var input = event.target;
            // Ensure that you have a file before attempting to read it
            if (input.files && input.files[0]) {
                // create a new FileReader to read this image and convert to base64 format
                var reader = new FileReader();
                // Define a callback function to run, when FileReader finishes its job
                reader.onload = (e) => {
                    // Note: arrow function used here, so that "this.imageData" refers to the imageData of Vue component
                    // Read image as base64 and set to imageData
                    this.$set(this.item,input.name,e.target.result);
                }
                // Start the reader job - read file as a data url (base64 format)
                reader.readAsDataURL(input.files[0]);
            }
        },
        clearImage: function(item,field){
    	    item.__data__[field] = '';
            let r = {'path':item.__path__,'key':field,'value':item.__data__[field],'context':{}};
            this.send('.ws-dummy',['_cache','cache',this.guid,r]);
        },
        _buildItem (){
 			let item = {__data__:{},__containers__:{}}
 			for(let i = 0,field = '',fields = Object.keys(this.view.columns); i < fields.length;i++ ){
 				field = fields[i];
 				switch(this.meta.columns[field].type){
					case 'many2one':
					case 'related':
						item.__data__[field] = {id:null,name:null};
						break;
					case 'one2many':
						item.__containers__[field] = [];
						break;
					case 'many2many':
						break;
					case 'datetime':
						item.__data__[field] = null;
						break;
					case 'date':
						item.__data__[field] = null;
						break;
					case 'time':
						item.__data__[field] = null;
						break;
					case 'binary':
						item.__data__[field] = '';
						break;
					case 'referenced':
						if (['many2one','related'].indexOf(this.meta.columns[field].reftype) != -1) {
							item.__data__[field] = {id:null,name:null};
							}
						else {
							item.__data__[field] = null;							
							}
						break;
					default:
						item.__data__[field] = null;
					}
				if (field in this.meta.default) {
					item.__data__[field] = this.meta.default[field];
					}
				}
				
					return item;			
			},
        buildFormFields (){
 			let c = [];
 			for(let i = 0,fields = Object.keys(this.view.columns); i < fields.length;i++ ){
 				if (['one2many'].indexOf(this.meta.columns[fields[i]].type) < 0) c.push(fields[i]);
 				else if (this.o2mfields.indexOf(fields[i]) < 0) this.o2mfields.push(fields[i]);
 				if (['date','time','datetime'].indexOf(this.meta.columns[fields[i]].type) < 0) this.menu[fields[i]] = false;
			}
			//console.log('formfield:',c);
			return c;
			},
        close () {
          this.dialog = false
          this.$destroy();
          this.$el.remove();
        },
	    prepareForSave(meta,item,mode){
			let record,containers;
			if ('__data__' in item ) record = item.__data__;
			else record = item;
			if ('__containers__' in item) containers = item.__containers__;
			else containers = {};
			let r = {},ct;
	          for(let k in record){
				  if ( k == 'id' && mode == 'new') continue;
				  if (k == 'id') ct = 'uuid';
				  else ct = meta.columns[k].type;
				  switch(ct){
					 case 'many2one':
					 case 'related':
						if (mode === 'edit' || mode ==='new' && record[k].id != null) {if (record[k] != null && record[k].id != null && record[k].id.length == 36) r[k] = record[k].id; else r[k] = null;}
						break;
					case 'many2many':
						r[k] = []
						for(let i = 0; i < record[k].length;i++){
							r[k].push(this.prepareForSave(this.metas[meta.columns[k].obj].meta,record[k][i],mode).id);
							}
						break;
					 case 'referenced':
						break;
					 case 'boolean':
						if (mode =='new' && record[k] != null || mode == 'edit') {if (record[k] != null && record[k])r[k] = record[k]; else r[k] = null;}
						break;
					 case 'integer':
						if (mode === 'edit' || mode ==='new' && record[k] != null) {if (record[k] != null) r[k] = parseInt(record[k],10); else r[k] = null;}
						break;
					 case 'float':
					 case 'double':
					 case 'real':
						if (mode === 'edit' || mode ==='new' && record[k] != null) {if (record[k] != null) r[k] = parseFloat(record[k]); else r[k] = null;}
						break;					 
					 case 'decimal':
					 case 'numeric':
						if (mode === 'edit' || mode ==='new' && record[k] != null) {if (record[k] != null) r[k] = {'__decimal__':record[k]}; else r[k] = null;}
						break;
					case 'datetime':
						if (mode === 'edit' || mode ==='new' && record[k] != null) {if (record[k] != null) if (meta.columns[k].timezone) r[k] = {'__datetime_tz__':record[k] instanceof Date ?record[k].toJsonString(): record[k] }; else r[k] = {'__datetime__':record[k] instanceof Date ?record[k].toJsonString():record[k]}; else r[k] = null;} 
						break;
					case 'date':
						if (mode === 'edit' || mode ==='new' && record[k] != null) {if (record[k] != null) r[k] = {'__date__':record[k]}; else r[k] = null;}
						break;
					case 'time':
						if (mode === 'edit' || mode ==='new' && record[k] != null) {if (record[k] != null) if (meta.columns[k].timezone) r[k] = {'__time_tz__':record[k]}; else r[k] = {'__time__':record[k]}; else r[k] = null;}
						break;
					case 'timedelta':
						if (mode === 'edit' || mode ==='new' && record[k] != null) {if (record[k] != null) r[k] = {'__timedelta__':record[k]}; else r[k] = null;}
						break;
					 default:
						if (mode === 'edit' || mode ==='new' && record[k] != null) {if (record[k] != null && record[k].length > 0) r[k] = record[k]; else r[k] = null;}
				  }
			  }
			for(let k in containers){
				r[k] = []
				for(let i = 0; i < containers[k].length;i++){
					r[k].push(this.prepareForSave(this.metas[meta.columns[k].obj].meta,containers[k][i],mode));
					}
			}
			  //console.log('record:',r);
			  return r;
		},
        save () {
          let record;
          if (this.mode == 'lookup' || this.mode == 'edit') {
            record = this.prepareForSave(this.meta,this.item,'edit');
            this.send('onSave',['_cache','save',this.guid,{}]);
          } else {
            record = this.prepareForSave(this.meta,this.item,'new');
            if (Object.keys(record).length > 0) this.send('onSave',['_cache','save',this.guid,{}]);
          }
      },	
	   onSave(msg){
		if (msg[0] == 'commit') this.send('onUpdate',['models',this.model,'read',{'fields':this.fields,'ids':msg[1]}]);
		if (msg[0] == 'no chache') this.$snotify.info('No cache.');
		 },
	  onInitialize(msg){
		  this.$set(this,'item',msg[0]);
		  this.formfields = this.buildFormFields();
		  },
	  onUpdate(msg){
		let v = {},rec_name=this.meta.names.rec_name ? this.meta.names.rec_name: 'value';
		switch(this.role){
			case 'many2one-new':
				v['obj'] = this.obj;
				v['rel'] = this.rel;
				v['v'] = {id:msg[0].id,name:msg[0][rec_name],idx:this.idx,item:this.item_find};
				this.$websocket._components[this.obj].m2o_new(v['rel'],v['v']);
				break;
			case 'related-new':
				v['obj'] = this.obj;
				v['rel'] = this.rel;
				v['v'] = {id:msg[0].id,name:msg[0][rec_name],idx:this.idx,item:this.item_find};
				this.$websocket._components[this.obj].related_new(v['rel'],v['v']);
				break;
			}
		this.send('.ws-log',['_cache','commit',this.guid,{'action':'commit work'}]);
		this.$snotify.info('Record saved.');
		this.dialog = false;
		},
	onLoadMeta: function(msg){
		if (this.modal){
			this.model = msg[0]['root'];
			this.metas = msg[0]['models'];
			this.meta = this.metas[this.model].meta;
			this.view = this.metas[this.model].views.form;
			this.name = this.meta.description.split(' ').slice(2).join(' ');
			this.actions = this.meta.actions;
			this.$set(this,'fields',this._fieldsBuild(this.model,Object.keys(this.view.columns),this.meta.schema));
			this.item = this._buildItem();
			}
			if (this.role == 'many2one-detail' || this.role == 'related-detail') {
			this.formfields = this.buildFormFields();
			this.send('onRead',['models',this.model,'read',{'fields':this.fields,'ids':this.item_find.__data__[this.rel].id,'context':{'cache':this.guid}}]);
			}
			else this.send('onInitialize',['_cache','initialize',this.guid,{'model':this.model,'view':'form'}]);
		
			this.$set(this,'root',`${this.$options.name}:${this._uid}`);
		},
	onOpen(msg){
		if (this.guid == null) this.guid = msg[0];
		switch(this.mode){
			case 'new':
				if (this.modal) this.send('onLoadMeta',['uis','get_view_by_name_v2',{'name':'view.'+this.model+'.form'}]);
				else {
					this.send('onInitialize',['_cache','initialize',this.guid,{'model':this.model,'view':'form'}]);
					this.$set(this,'root',`${this.$options.name}:${this._uid}`);
					}
				break;
			case 'lookup':
			case 'edit':
				if (this.modal && (this.role == 'many2one-detail' || this.role == 'related-detail')) this.send('onLoadMeta',['uis','get_view_by_name_v2',{'name':'view.'+this.model+'.form'}]);
				else {
				this.item = this._buildItem();
				this.formfields = this.buildFormFields();
				this.$set(this,'root',`${this.$options.name}:${this._uid}`);
				this.send('onRead',['models',this.model,'read',{'fields':this.fields,'ids':this.selected[0].id,'context':{'cache':this.guid}}]);
			}
		}
		},
	do_action(name,item){
		this.send('onAction',['_cache','action',this.guid,{'path':item.a.path,'name':name}]);
		},
	onAction(msg){
		console.log('On Action MSG:',msg);
		},
	dataRowContainer(containers,parent){
		for(let k in containers) {
			if (!(k+'.'+parent in this.c)) this.$set(this.c,k+'.'+parent,containers[k]);
			for(let i = 0; i < containers[k].length;i++) this.dataRow(containers[k][i]);		
		}
		},
	dataRow(row){
		if ('__data__' in row) this.$set(this.d,row['__path__'],row.__data__);
		if ('__meta__' in row) this.$set(this,'m',row.__meta__[row['__model__']])
		//console.log('M:',this.m);
		if ('__m2m_containers__' in row) this.dataRowContainer(row['__m2m_containers__'],row['__path__']);
		if ('__o2m_containers__' in row) this.dataRowContainer(row['__o2m_containers__'],row['__path__']);
		},
	onRead: function(rows){
		console.log('rows:',rows[0]);
		if (rows.length > 0) {

			this.c = {};
			this.d = {};
			this.m = rows[0]['__meta__'];

			this.item = rows[0];
			this.dataRow(this.item);
			console.log('item:',this.item);
			}
			else {
				this.item = this._buildItem();
				this.d = {};
				this.c = {};
				this.m = {};
				}
		this.$set(this,'root',`${this.$options.name}:${this._uid}`);
		}
	},
	created: function(){
		if (this.mode == 'new') this.$set(this,'root',`${this.$options.name}:${this._uid}`);
		},
	mounted: function(){
		if (!this.modal) { 
			this.meta = this.metas[this.model].meta;
			this.views = this.metas[this.model].views;
			this.view = this.views.form;
			this.name = this.meta.description.split(' ').slice(2).join(' ');			
			this.$set(this,'fields',this._fieldsBuild(this.model,Object.keys(this.view.columns),this.meta.schema));
			}
			this.$websocket.registerComponent({n:`${this.$options.name}:${this._uid}`,c:this});
			this.send('onOpen',['_cache','open',{'mode':this.mode,'context':{}}]);
		},
	beforeDestroy: function(){
		this.$websocket.unregisterComponent(`${this.$options.name}:${this._uid}`);
		if (!this.modal){
			this.send('.ws-dummy',['_cache','close',this.guid]);
			}
		},
	activated: function(){
		if (this.guid != null)this.send('.ws-log',['_cache','setmode',this.guid,{'mode':this.mode}]);
		},
}

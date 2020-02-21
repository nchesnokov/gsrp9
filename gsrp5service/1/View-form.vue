<template>
	<v-card>
        <v-card-title>
          <span class="headline">{{ mode }}: {{ name }}</span>
        </v-card-title>
        <v-card-text>
          <v-container fluid>
            <v-layout 
			    v-touch="{
			      left: () => swipe('Left'),
			      right: () => swipe('Right'),
			      up: () => swipe('Up'),
			      down: () => swipe('Down')
			    }"
            column>
              <v-form v-model="valid" ref="form" lazy-validation>
                <template v-if="Object.keys(actions).length > 0">
						<h3>Actions</h3>
						<v-layout row>
							<v-btn v-for="(action,akey) in actions" :key="akey" fab dark small color="purple darken-2" @click="do_action(akey,item)">{{ action.icon }}</v-btn>
						</v-layout>
                </template>
				<template v-for="field in formfields">
					<template v-if="['char','varchar'].indexOf(meta.columns[field].type) >= 0">
						<v-text-field v-model="item[field]" :rules="rules[field]" :label="meta.columns[field].label" :readonly="readonly(field)" :required="required(field)" v-show="visible(field)" @change="cache(item,field)" clearable  :counter="meta.columns[field].size!=null ? meta.columns[field].size : 1024"></v-text-field>
					</template>
					<template v-else-if="['text','xml','jsonb'].indexOf(meta.columns[field].type) >= 0">
						<v-textarea v-model="item[field]" :rules="rules[field]" :label="meta.columns[field].label" :readonly="readonly(field)" :required="required(field)" v-show="visible(field)" @change="cache(item,field)" clearable  :counter="meta.columns[field].size!=null ? meta.columns[field].size : 1024"></v-textarea>
					</template>
					<template v-else-if="meta.columns[field].type == 'many2one'">
						<v-layout row v-show="visible(field)">
							<v-text-field v-model="item[field].name" :rules="rules[field]" :label="meta.columns[field].label" :readonly="readonly(field)" :required="required(field)" @change="m2o_cache(item,field)" clearable></v-text-field>
							<v-icon fab dark small color="primary" @click="on_new_many2one(item,field)">add</v-icon>
							<v-icon fab dark small color="primary" @click="on_find_many2one(item,field)">search</v-icon>
						</v-layout>
					</template>

					<template v-else-if="meta.columns[field].type == 'related'">
						<v-layout row v-show="visible(field)">
							<v-text-field v-model="item[field].name" :rules="rules[field]" :label="meta.columns[field].label" :readonly="readonly(field)" :required="required(field)" @change="related_cache(item,field,meta.columns[field].relatedy)" clearable></v-text-field>
							<v-icon fab dark small color="primary" @click="on_new_related(item,field)">add</v-icon>
							<v-icon fab dark small color="primary" @click="on_find_related(item,field)">search</v-icon>
						</v-layout>
					</template>


					<template v-else-if="meta.columns[field].type == 'selection'">
						<v-autocomplete v-model="item[field]" :label="meta.columns[field].label" :disabled="readonly(field)" :required="required(field)" v-show="visible(field)" :items="selectionFrom[field]" @change="cache(item,field)" :prepend-icon="meta.columns[field].compute != null ? 'functions':''" hide-details></v-autocomplete>
					</template>
					<template v-else-if="meta.columns[field].type == 'boolean'">
						<v-checkbox v-model="item[field]" :label="meta.columns[field].label" :disabled="readonly(field)" :required="required(field)" v-show="visible(field)" @change="cache(item,field) ":prepend-icon="meta.columns[field].compute != null ? 'functions':''" hide-details></v-checkbox>
					</template>
					<template v-else-if="meta.columns[field].type == 'datetime'">
						<v-datetime-picker v-model="item[field]" :label="meta.columns[field].label" :readonly="readonly(field)" :required="required(field)" v-show="visible(field)" locale="ru-ru" format="YYYY-MM-DD HH:mm:ss" @change="cache(item,field)" ></v-datetime-picker>
					</template>
					<template v-else-if="meta.columns[field].type == 'date'">
				      <v-menu
				        :ref="field"
				        v-model="menu[field]"
				        :close-on-content-click="false"
				        :nudge-right="40"
				        :return-value.sync="item[field]"
				        lazy
				        transition="scale-transition"
				        offset-y
				        full-width
				        min-width="290px"
				      >
				        <template v-slot:activator="{ on }">
				          <v-text-field
				            v-model="item[field]"
				            :label="meta.columns[field].label"
				            prepend-icon="event"
				            readonly
				            v-on="on"
				          ></v-text-field>
				        </template>
				        <v-date-picker v-model="item[field]" :label="meta.columns[field].label" :readonly="readonly(field)" :required="required(field)" v-show="visible(field)" locale="ru-ru" color="green lighten-1" @change="cache(item,field)"  no-title scrollable></v-date-picker>
				          <v-spacer></v-spacer>
				          <v-btn text color="primary" @click="menu[field] = false">Cancel</v-btn>
				          <v-btn text color="primary" @click="$refs[field][0].save(item[field])">OK</v-btn>
				        </v-date-picker>
				      </v-menu>
						
					</template>
					<template v-else-if="meta.columns[field].type == 'time'">
				      <v-menu
				        :ref="field"
				        v-model="menu[field]"
				        :close-on-content-click="false"
				        :nudge-right="40"
				        :return-value.sync="item[field]"
				        lazy
				        transition="scale-transition"
				        offset-y
				        full-width
				        max-width="290px"
				        min-width="290px"
				      >
				        <template v-slot:activator="{ on }">
				          <v-text-field
				            v-model="item[field]"
				            :label="meta.columns[field].label"
				            prepend-icon="access_time"
				            readonly
				            v-on="on"
				          ></v-text-field>
				        </template>
				        <v-time-picker v-model="item[field]" :label="meta.columns[field].label" :readonly="readonly(field)" :required="required(field)" v-show="visible(field)" @change="cache(item,field)" :prepend-icon="meta.columns[field].compute != null ? 'functions':''" ></v-time-picker>
				      </v-menu>
					</template>
					<template v-else-if="meta.columns[field].type == 'timedelta'">
						<v-text-field v-model="item[field]" :label="meta.columns[field].label" :readonly="readonly(field)" :required="required(field)" v-show="visible(field)" @change="cache(item,field)" clearable :prepend-icon="meta.columns[field].compute != null ? 'functions':''" ></v-text-field>
					</template>
					<template v-else-if="meta.columns[field].type == 'integer'">
						<v-text-field v-model="item[field]" :rules="rules[field]" :label="meta.columns[field].label" :readonly="readonly(field)" :required="required(field)" v-show="visible(field)" @change="cache(item,field)" clearable :prepend-icon="meta.columns[field].compute != null ? 'functions':''" ></v-text-field>
					</template>
					<template v-else-if="meta.columns[field].type == 'float'">
						<v-text-field v-model="item[field]" :rules="rules[field]" :label="meta.columns[field].label" :readonly="readonly(field)" :required="required(field)" v-show="visible(field)" @change="cache(item,field)" clearable :prepend-icon="meta.columns[field].compute != null ? 'functions':''" ></v-text-field>
					</template>
					<template v-else-if="meta.columns[field].type == 'double'">
						<v-text-field v-model="item[field]" :rules="rules[field]" :label="meta.columns[field].label" :readonly="readonly(field)" :required="required(field)" v-show="visible(field)" @change="cache(item,field)" clearable :prepend-icon="meta.columns[field].compute != null ? 'functions':''" ></v-text-field>
					</template>
					<template v-else-if="meta.columns[field].type == 'real'">
						<v-text-field v-model="item[field]" :rules="rules[field]" :label="meta.columns[field].label" :readonly="readonly(field)" :required="required(field)" v-show="visible(field)" @change="cache(item,field)" clearable :prepend-icon="meta.columns[field].compute != null ? 'functions':''" ></v-text-field>
					</template>
					<template v-else-if="meta.columns[field].type == 'decimal'">
						<v-text-field v-model="item[field]" :rules="rules[field]" :label="meta.columns[field].label" :readonly="readonly(field)" :required="required(field)" v-show="visible(field)" @change="cache(item,field)" clearable :prepend-icon="meta.columns[field].compute != null ? 'functions':''" ></v-text-field>
					</template>
					<template v-else-if="meta.columns[field].type == 'numeric'">
						<v-text-field v-model="item[field]" :rules="rules[field]" :label="meta.columns[field].label" :readonly="readonly(field)" :required="required(field)" v-show="visible(field)" lazy clearable @change="cache(item,field)" :prepend-icon="meta.columns[field].compute != null ? 'functions':''" ></v-text-field>
					</template>

					<template v-else-if="meta.columns[field].type == 'binary'">
						<v-card v-show="visible(field)">
							<v-card-title>
								<span>{{ meta.columns[field].label }}</span>
							</v-card-title>
							<v-responsive>
								<v-img class="preview" :src="item[field]?item[field]:''" width="128px" height="128px"></v-img>	
							</v-responsive>
							<v-card-actions>
								<div class="image-preview">
									<input type="file" @change="previewImage" :accept="meta.columns[field].accept" :name="field" :disabled="readonly(field)"/>
									<v-icon @click="item[field] = ''" v-if="item[field] != null && item[field].length > 0"> clear</v-icon>
								</div>							
							</v-card-actions>
						</v-card>
					</template>
					<template v-else-if="meta.columns[field].type == 'many2many'">
						<gsrp5-m2mlist-view :metas="metas" :meta="metas[meta.columns[field].obj].meta" :model="meta.columns[field].obj" :view="metas[meta.columns[field].obj].views.m2mlist" :items="item[field]" :field="field" :item_find="item"></gsrp5-m2mlist-view>
					</template>
					
					
					<template v-else-if="meta.columns[field].type == 'referenced'">
						<template v-if="['many2one','related'].indexOf(meta.columns[field].reftype) >= 0">{{ item[field].name }}</template>
						<template v-else-if="meta.columns[field].reftype == 'selection'">{{ selectionFromForm[field][item[field]] }}</template>
						<template v-else-if="meta.columns[field].reftype == 'datetime'">{{ item[field] | formatDatetime  }}</template>
						<template v-else-if="meta.columns[field].reftype == 'date'">{{ item[field] | formatDate  }}</template>
						<template v-else-if="meta.columns[field].reftype == 'time'">{{ item[field] | formatTime  }}</template>
						<template v-else-if="meta.columns[field].reftype == 'timedelta'">{{ item[field] | formatTimedelta  }}</template>
						<template v-else-if="meta.columns[field].reftype == 'integer'">{{ item[field] }}</template>
						<template v-else-if="meta.columns[field].reftype == 'float'">{{ item[field] }}</template>
						<template v-else-if="meta.columns[field].reftype == 'double'">{{ item[field] }}</template>
						<template v-else-if="meta.columns[field].reftype == 'real'">{{ item[field] }}</template>
						<template v-else-if="meta.columns[field].reftype == 'decimal'">{{ item[field] }}</template>
						<template v-else-if="meta.columns[field].reftype == 'numeric'">{{ item[field] }}</template>
						<template v-else>{{ item[field] }}</template>
					</template>
					<template v-else>
						<v-text-field v-model="item[field]" :rules="rules[field]" :label="meta.columns[field].label" :readonly="readonly(field)" :required="required(field)" v-show="visible(field)" @change="cache(item,field)" clearable :prepend-icon="meta.columns[field].compute != null ? 'functions':''" ></v-text-field>
				     </template>
				   </template>
			      <v-card text>						  
			        <v-card-text>
			        <v-flex xs12 sm12 md12 lg12 xl12>
						<v-tabs v-model="active">
							<v-tabs-slider color="yellow"></v-tabs-slider>
							<v-tab  v-for="(o2mfield,index) in o2mfields" :key="index" :href="'#tab-'+o2mfield" v-show="visible(o2mfield)">
								{{ meta.columns[o2mfield].label }}
							</v-tab>
							<v-tabs-items>
								<v-tab-item  v-for="(o2mfield,index) in o2mfields" :key="index" :value="'tab-' + o2mfield">
									<gsrp5-tabs-o2m-component :metas="metas" :meta="metas[meta.columns[o2mfield].obj].meta" :model="meta.columns[o2mfield].obj" :views="metas[meta.columns[o2mfield].obj].views" :items="item[o2mfield]" :rel="meta.columns[o2mfield].rel" :mode="(mode == 'readonly' || readonly(o2mfield)) ? 'readonly':mode" role="role" :o2mfield="o2mfield" :root="root" :guid="guid" :container="item['a'].path+'.'+o2mfield" :parent="item['a'].path"></gsrp5-tabs-o2m-component>
								</v-tab-item>
							</v-tabs-items>
						</v-tabs>					
			        </v-flex>
			        </v-card-text>
			      </v-card>
			  </v-form>
            </v-layout>
          </v-container>
        </v-card-text>
        <v-card-actions v-if="!modal">
          <v-spacer></v-spacer>
			<v-btn color="blue darken-1" text @click.native="close" v-if="modal">Cancel</v-btn>
			<v-btn color="error" text @click.native="clear" :disabled="mode == 'lookup'" v-else>Clear</v-btn>
          <v-btn :disabled="mode == 'lookup'  || !valid" color="blue darken-1" text @click.native="save">Save</v-btn>
          <v-btn :disabled="mode == 'lookup'" color="success" text @click.native="validate">Validate</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script src="./js/view-form.js"></script>

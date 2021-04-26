__all__ = ['standart_gen_script_el_form','standart_gen_script_el_form_modal','standart_gen_empty_style','standart_gen_empty_scoped_style']

def standart_gen_empty_style(info,columns):
	return """
<style lang="css">
<style>	
	"""

def standart_gen_empty_scoped_style(info,columns):
	return """
<style scoped lang="css">
<style>	
	"""


def standart_gen_script_el_form(info,columns):
	return 	"""
<script>	
	import {
	    defineComponent,
	    defineAsyncComponent,
	    onMounted,
	    ref,
	    reactive,
	    getCurrentInstance,
	    render,
	    createVNode
	}
	from 'vue'
	
	export default defineComponent({
	    name: 'gp-form',
	    props: ['cid', 'metas', 'model'],
	    setup(props) {
	        const {
	            proxy
	        } = getCurrentInstance()
	        const mode = ref('new')
	        const page = ref(1)
	        const pageSize = ref(1)
	        const showSearch = ref(false)
	        const colsType = reactive({})
	        const colsLabel = reactive({})
	        const colsTranslate = reactive({})
	        const colsLang = reactive({})
	        const dataForm = reactive({})
	        const selOptions = reactive({})
	        const fields = reactive([])
	        const cols = reactive([])
	        const o2mcols = reactive([])
	        const multipleSelection = reactive([])
	
	        const readonly = col => {
	            return mode.value == 'lookup' || isCompute(col)
	        }
	
	        const i18nCommand = (command) =>{
	          console.log('command-18n:',command)
	          colsLang[command.col] = command.lang
	        };
	        const handleSelectionChange = val => {
	            console.log('selection:', val)
	            multipleSelection.splice(0, multipleSelection.length, ...val)
	        }
	
	        const handleCurrentChange = val => {
	            page.value = val
	            proxy.$websocket.send({
	                    _msg: [
	                        props.cid,
	                        'models',
	                        props.model,
	                        'read', {
	                            fields: fields,
	                            ids: multipleSelection[page.value - 1],
	                            context: proxy.$UserPreferences.Context
	                        }
	                    ]
	                },
	                on_read
	            )
	        }
	
	        const isCompute = col => {
	            return (
	                ('compute' in props.metas[props.model].meta.columns[col] &&
	                    props.metas[props.model].meta.columns[col].compute != null) ||
	                colsType[col] == 'composite'
	            )
	        }
	
	        const _get_selections = s => {
	            let r = []
	            for (let j = 0; j < s.length; j++) r.push({
	                label: s[j][1],
	                value: s[j][0]
	            })
	            return r
	        }
	
	        const on_find_new = (value, opts) => {
	            console.log('on_find_new:', value, opts)
	            if (
	                ['new', 'edit'].indexOf(mode.value) >= 0 &&
	                value.id &&
	                value.id.length > 0 &&
	                value.name &&
	                value.name.length > 0
	            )
	                dataForm[opts.col] = value
	        }
	
	        const fieldsBuild = (model, view) => {
	            let fcols = []
	            for (let i = 0, columns = Object.keys(props.metas[model].views[view].columns), k = {}; i < columns.length; i++)
	                switch (props.metas[model].meta.columns[columns[i]].type) {
	                    case 'one2many':
	                        k = {}
	                        if (props.metas[model].meta.columns[columns[i]].obj != model)
	                            k[columns[i]] = fieldsBuild(props.metas[model].meta.columns[columns[i]].obj, 'form')
	                        else k[columns[i]] = Object.keys(props.metas[model].views.list.columns)
	                        fcols.push(k)
	                        break
	                    case 'many2many':
	                        k = {}
	                        k[columns[i]] = Object.keys(
	                            props.metas[props.metas[model].meta.columns[columns[i]].obj].views.m2mlist.columns
	                        )
	                        fcols.push(k)
	                        break
	                    default:
	                        fcols.push(columns[i])
	                }
	            return fcols
	        }
	
	        const do_find = col => {
	            const rootComponent = defineAsyncComponent({
	                loader: () =>
	                    import ('./gp-find.vue'),
	                suspensible: false
	            })
	            const rootProps = {
	                cid: props.cid,
	                model: props.metas[props.model].meta.columns[col].obj,
	                mode: 'single',
	                callback: on_find_new,
	                callbackOpts: {
	                    col: col,
	                    mode: 'find'
	                }
	            }
	            const vnode = createVNode(rootComponent, rootProps)
	            vnode.appContext = proxy.$appcontext
	            const rootContainer = document.createElement('div')
	            render(vnode, rootContainer, false)
	            document.body.appendChild(rootContainer)
	            console.log('do-search!', col, vnode, proxy)
	        }
	
	        const do_search = event => {
	            proxy.$websocket.send({
	                    _msg: [
	                        props.cid,
	                        'models',
	                        props.model,
	                        'search', {
	                            cond: event.cond,
	                            context: proxy.$UserPreferences.Context,                            
	                            offset: event.offset.value,
	                            limit: event.limit.value
	                            }
	                    ]
	                },
	                on_search
	            )
	        }
	
	        const on_search = msg => {
	            console.log('on-search:', msg)
	            if (msg.length > 0) {
	                multipleSelection.splice(0, multipleSelection.length, ...msg)
	                showSearch.value = false
	                mode.value = 'edit'
	                proxy.$websocket.send({
	                        _msg: [
	                            props.cid,
	                            'models',
	                            props.model,
	                            'read', {
	                                fields: fields,
	                                ids: multipleSelection[page.value - 1],
	                                context: proxy.$UserPreferences.Context
	                            }
	                        ]
	                    },
	                    on_read
	                )
	            }
	        }
	        const do_modal_form = (col, oid, mode) => {
	            const rootComponent = defineAsyncComponent({
	                loader: () =>
	                    import ('./gp-form-modal.vue'),
	                suspensible: false
	            })
	            const rootProps = {
	                cid: props.cid,
	                model: props.metas[props.model].meta.columns[col].obj,
	                oid: oid,
	                mode: mode
	            }
	            if (mode === 'new') {
	                rootProps.callback = on_find_new
	                rootProps.callbackOpts = {
	                    col: col,
	                    mode: 'new'
	                }
	            }
	            const vnode = createVNode(rootComponent, rootProps)
	            vnode.appContext = proxy.$appcontext
	            const rootContainer = document.createElement('div')
	            render(vnode, rootContainer, false)
	            document.querySelector('#sv').appendChild(rootContainer)
	        }
	
	        const do_action = action => {
	            console.log('action:', action)
	            switch (action) {
	                case 'new':
	                    mode.value = 'new'
	                    break
	                case 'edit':
	                    mode.value = 'edit'
	                    break
	                case 'lookup':
	                    mode.value = 'lookup'
	                    break
	                case 'find':
	                    showSearch.value = true
	                    break
	            }
	        }
	
	        const do_add = col => {
	            do_modal_form(col, null, 'new')
	            console.log('do-add!', col)
	        }
	
	        const do_edit = (col, oid) => {
	            do_modal_form(col, oid, 'edit')
	            console.log('do-edit!', col, oid)
	        }
	
	        const do_lookup = (col, oid) => {
	            do_modal_form(col, oid, 'lookup')
	            console.log('do-lookup!', col, oid)
	        }
	
	        const onSubmit = () => {
	            console.log('submit!')
	        }
	
	        const onValidate = () => {
	            console.log('validate')
	        }
	
	        const onCancel = () => {
	            console.log('cancel!')
	            for (
	                let i = 0,
	                    c = Object.keys(props.metas[props.model].views.form.columns),
	                    meta = props.metas[props.model].meta.columns; i < c.length; i++
	            ) {
	                switch (meta[c[i]].type) {
	                    case 'many2one':
	                        dataForm[c[i]] = {
	                            id: null,
	                            name: null
	                        }
	                        break
	                    case 'one2many':
	                    case 'many2many':
	                        dataForm[c[i]] = []
	                        break
	                    case 'selection':
	                        dataForm[c[i]] = ''
	                        break
	                    case 'boolean':
	                        dataForm[c[i]] = false
	                        break
	                    default:
	                        dataForm[c[i]] = ''
	                }
	            }
	        }
	
	        const on_read = msg => {
	            console.log('on_read:', msg)
	            if (msg && msg.length > 0) Object.assign(dataForm, msg[0])
	        }
	
	        onMounted(() => {
	            for (
	                let i = 0,
	                    c = Object.keys(props.metas[props.model].views.form.columns),
	                    meta = props.metas[props.model].meta.columns; i < c.length; i++
	            ) {
	                colsType[c[i]] = meta[c[i]].type
	                colsLabel[c[i]] = meta[c[i]].label
	                colsTranslate[c[i]] = 'translate' in meta[c[i]] ? meta[c[i]].translate:false
	                colsLang[c[i]] = proxy.$UserPreferences.lang
	                if (colsType[c[i]] == 'one2many') o2mcols.push(c[i])
	                else cols.push(c[i])
	
	                switch (meta[c[i]].type) {
	                    case 'many2one':
	                        dataForm[c[i]] = {
	                            id: null,
	                            name: null
	                        }
	                        break
	                    case 'one2many':
	                    case 'many2many':
	                        dataForm[c[i]] = []
	                        break
	                    case 'selection':
	                        selOptions[c[i]] = _get_selections(meta[c[i]].selections)
	                        dataForm[c[i]] = ''
	                        break
	                    case 'boolean':
	                        dataForm[c[i]] = false
	                        break
	                    default:
	                        dataForm[c[i]] = ''
	                }
	            }
	            console.log('translate:',colsTranslate,colsType)
	            fields.splice(0, fields.length, ...fieldsBuild(props.model, 'form'))
	            if (mode.value !== 'new')
	                proxy.$websocket.send({
	                        _msg: [props.cid, 'models', props.model, 'select', {
	                            fields: fields,
	                            context: proxy.$UserPreferences.Context,
	                            limit: 1
	                        }]
	                    },
	                    on_read
	                )
	                //console.log('fields:',fields);
	        })
	        return {
	            mode,
	            readonly,
	            i18nCommand,
	            isCompute,
	            showSearch,
	            page,
	            pageSize,
	            multipleSelection,
	            handleCurrentChange,
	            handleSelectionChange,
	            colsType,
	            colsLabel,
	            colsTranslate,
	            colsLang,
	            dataForm,
	            selOptions,
	            fields,
	            cols,
	            o2mcols,
	            fieldsBuild,
	            onSubmit,
	            onValidate,
	            onCancel,
	            do_search,
	            on_search,
	            do_action,
	            do_find,
	            do_add,
	            do_edit,
	            do_lookup,
	            on_find_new,
	            on_read
	        }
	    }
	})
<script>		
	"""


def standart_gen_script_el_form_modal(info,columns):
	return 	"""
<script>

import {
    defineComponent,
    defineAsyncComponent,
    onMounted,
    reactive,
    ref,
    getCurrentInstance,
    render,
    createVNode,
    computed
}
from 'vue'

export default defineComponent({
    name: 'gp-form-modal',
    props: {
        cid: {
            type: String,
            required: true
        },
        oid: {
            type: [String, Object],
            default: null
        },
        model: {
            type: String,
            required: true
        },
        mode: {
            type: String,
            default: 'new'
        },
        callback: {
            type: Function,
            default: function() {
                return null
            }
        },
        callbackOpts: {
            type: Object,
            default: function() {
                return {}
            }
        }
    },
    setup(props) {
        const {
            proxy
        } = getCurrentInstance()
        const showDialog = ref(true)
        const visible = ref(false)
        const page = ref(1)
        const pageSize = ref(1)
        const metas = reactive({})
        const colsType = reactive({})
        const colsLabel = reactive({})
        const dataForm = reactive({})
        const selOptions = reactive({})
        const fields = reactive([])
        const cols = reactive([])
        const o2mcols = reactive([])

        const title = computed(() => {
            return props.mode + ':' + (Object.keys(metas).length > 0 ? metas[props.model].meta.description : ref(''))
        })

        const readonly = col => {
            return props.mode == 'lookup' || isCompute(col)
        }

        const isCompute = col => {
            return (
                ('compute' in metas[props.model].meta.columns[col] && metas[props.model].meta.columns[col].compute != null) ||
                colsType[col] == 'composite'
            )
        }

        const handleCurrentChange = val => {
            visible.value = true
            page.value = val
            proxy.$websocket.send({
                    _msg: [
                        props.cid,
                        'models',
                        props.model,
                        'read', {
                            fields: fields,
                            ids: props.oid[page.value - 1],
                            context: proxy.$UserPreferences.Context
                        }
                    ]
                },
                on_read
            )
        }

        const _get_selections = s => {
            let r = []
            for (let j = 0; j < s.length; j++) r.push({
                label: s[j][1],
                value: s[j][0]
            })
            return r
        }

        const fieldsBuild = (model, view) => {
            let fcols = []
            for (let i = 0, columns = Object.keys(metas[model].views[view].columns), k = {}; i < columns.length; i++)
                switch (metas[model].meta.columns[columns[i]].type) {
                    case 'one2many':
                        k = {}
                        if (metas[model].meta.columns[columns[i]].obj != model)
                            k[columns[i]] = fieldsBuild(metas[model].meta.columns[columns[i]].obj, 'form')
                        else k[columns[i]] = Object.keys(metas[model].views.list.columns)
                        fcols.push(k)
                        break
                    case 'many2many':
                        k = {}
                        k[columns[i]] = Object.keys(metas[metas[model].meta.columns[columns[i]].obj].views.m2mlist.columns)
                        fcols.push(k)
                        break
                    default:
                        fcols.push(columns[i])
                }
            return fcols
        }

        const on_find_new = (value, opts) => {
            console.log('on_find_new:', value, opts)
            if (['new', 'edit'].indexOf(props.mode) >= 0 && value.id.length > 0 && value.name.length)
                dataForm[opts.col] = value
        }

        const do_search = col => {
            const rootComponent = defineAsyncComponent({
                loader: () =>
                    import ('./gp-find.vue'),
                suspensible: false
            })
            const rootProps = {
                cid: props.cid,
                model: metas[props.model].meta.columns[col].obj,
                mode: 'single',
                callback: on_find_new,
                callbackOpts: {
                    col: col,
                    mode: 'find'
                }
            }
            if ('domain' in metas[props.model].meta.columns[col] && metas[props.model].meta.columns[col].domain != null) {
                let extcond = []
                for (let i = 0, domain = metas[props.model].meta.columns[col].domain; i < domain.length; i++)
                    extcond.push({
                        __tuple__: domain[i]
                    })
                rootProps.extcond = extcond
            }

            if (metas[props.model].meta.columns[col].type == 'related') {
                let extcond = [],
                    relatedy = metas[props.model].meta.columns[col].relatedy
                for (let i = 0; i < relatedy.length; i++)
                    extcond.push({
                        __tuple__: [relatedy[i], '=', dataForm[relatedy[i]].name]
                    })
                if ('extcond' in rootProps) rootProps.extcond.splice(0, 0, ...extcond)
                else rootProps.extcond = extcond
            }

            const vnode = createVNode(rootComponent, rootProps)
            vnode.appContext = proxy.$appcontext
            const rootContainer = document.createElement('div')
            render(vnode, rootContainer, false)
            document.querySelector('#sv').appendChild(rootContainer)
            console.log('do-search!', col, vnode, proxy)
        }

        const do_modal_form = (col, oid, mode) => {
            const rootComponent = defineAsyncComponent({
                loader: () =>
                    import ('./gp-form-modal.vue'),
                suspensible: false
            })
            const rootProps = {
                cid: props.cid,
                model: metas[props.model].meta.columns[col].obj,
                oid: oid,
                mode: mode
            }
            if (mode === 'new') {
                rootProps.callback = on_find_new
                rootProps.callbackOpts = {
                    col: col,
                    mode: 'new'
                }
            }
            const vnode = createVNode(rootComponent, rootProps)
            vnode.appContext = proxy.$appcontext
            const rootContainer = document.createElement('div')
            render(vnode, rootContainer, false)
            document.querySelector('#sv').appendChild(rootContainer)
        }

        const do_add = col => {
            do_modal_form(col, null, 'new')
            console.log('do-add!', col)
        }

        const do_edit = (col, oid) => {
            do_modal_form(col, oid, 'edit')
            console.log('do-edit!', col, oid)
        }

        const do_lookup = (col, oid) => {
            do_modal_form(col, oid, 'lookup')
            console.log('do-lookup!', col, oid)
        }

        const onSubmit = () => {
            console.log('submit!')
            if (props.callback != null && props.callbackOpts != null && props.callbackOpts.mode == 'new')
                props.callback({
                    id: dataForm.id,
                    name: dataForm[metas[props.model].meta.names.rec_name]
                }, props.callbackOpts)
            showDialog.value = false
        }

        const onValidate = () => {
            console.log('validate')
            showDialog.value = false
        }

        const onCancel = () => {
            console.log('cancel!')
            showDialog.value = false
        }

        const on_load_meta = msg => {
            console.log('on-load-meta:', msg)
            if (msg && msg.length > 0) Object.assign(metas, msg[0])
            for (
                let i = 0, c = Object.keys(metas[props.model].views.form.columns), meta = metas[props.model].meta.columns; i < c.length; i++
            ) {
                colsType[c[i]] = meta[c[i]].type
                colsLabel[c[i]] = meta[c[i]].label
                if (colsType[c[i]] == 'one2many') o2mcols.push(c[i])
                else cols.push(c[i])

                switch (meta[c[i]].type) {
                    case 'many2one':
                        dataForm[c[i]] = {
                            id: null,
                            name: null
                        }
                        break
                    case 'one2many':
                    case 'many2many':
                        dataForm[c[i]] = []
                        break
                    case 'selection':
                        selOptions[c[i]] = _get_selections(meta[c[i]].selections)
                        dataForm[c[i]] = ''
                        break
                    case 'boolean':
                        dataForm[c[i]] = false
                        break
                    default:
                        dataForm[c[i]] = ''
                }
            }
            fields.splice(0, fields.length, ...fieldsBuild(props.model, 'form'))
            console.log('props.oid:', props.oid)
            if (props.oid != null && ['edit', 'lookup'].indexOf(props.mode) >= 0)
                proxy.$websocket.send({
                        _msg: [
                            props.cid,
                            'models',
                            props.model,
                            'read', {
                                fields: fields,
                                ids: typeof props.oid == 'object' ? props.oid[0] : props.oid,
                                context: proxy.$UserPreferences.Context
                            }
                        ]
                    },
                    on_read
                )
        }

        const on_read = msg => {
            console.log('on_read:', msg)
            if (msg && msg.length > 0) Object.assign(dataForm, msg[0])
        }

        onMounted(() => {
            proxy.$websocket.send({
                    _msg: [props.cid, 'uis', 'get_meta_of_models_v2', {
                        model: props.model,
                        context: proxy.$UserPreferences.Context
                    }]
                },
                on_load_meta
            )
        })
        return {
            showDialog,
            visible,
            title,
            readonly,
            page,
            pageSize,
            handleCurrentChange,
            metas,
            isCompute,
            colsType,
            colsLabel,
            dataForm,
            selOptions,
            fields,
            cols,
            o2mcols,
            fieldsBuild,
            onSubmit,
            onValidate,
            onCancel,
            do_search,
            do_add,
            do_edit,
            do_lookup,
            on_find_new
        }
    }
})

</script>
"""

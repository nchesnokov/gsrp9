from .generatedefaultscript import *

__all__ = ['gen_template_el', 'gen_template_vuetify','gen_template_devextrme','gen_script_el','gen_script_vuetify','gen_script_devextrme','gen_style_el','gen_style_vuetify','gen_style_devextrme']

# framework element-plus template
def gen_template_el_form(info,columns):
	ci = info['columns']
	s = """
<template>	
	<slot name="search">
	    <el-row>
	        <gp-selectable v-if="showSearch" :columns="metas[model].meta.columns" :names="metas[model].meta.names" :cid="cid" @update:search="do_search" @update:search-cancel="showSearch = false"/>
	    </el-row>
	</slot>
	<slot>
	    <el-row>{{ mode +':' + metas[model].meta.description }}</el-row>
	    <el-row>
	       <el-dropdown @command="i18nCommand">
	          <span class="el-dropdown-link">
	            {{$UserPreferences.lang.toLowerCase()}}<i class="el-icon-arrow-down el-icon--right"></i>
	          </span>
	          <template #dropdown>
	            <el-dropdown-menu>
	              <el-dropdown-item v-for="lang in $UserPreferences.langs" :key=lang.code :command="{lang:lang.code}">{{lang.description}}</el-dropdown-item>
	            </el-dropdown-menu>
	          </template>
	        </el-dropdown>	
	    </el-row>
	    <el-row>
	        <el-button type="primary" size="mini" icon="el-icon-search" @click="do_action('find')"></el-button>
	        <el-button v-if="multipleSelection.length == 0" type="primary" size="mini" icon="el-icon-document-add" @click="do_action('new')"></el-button>
	        <el-button v-if="multipleSelection.length > 0" type="primary" size="mini" icon="el-icon-edit" @click="do_action('edit')"></el-button>
	        <el-button v-if="multipleSelection.length > 0" type="primary" size="mini" icon="el-icon-view" @click="do_action('lookup')"></el-button>
	    </el-row>
	    <el-pagination v-if="multipleSelection.length > 1" background layout="prev, pager, next" @current-change="handleCurrentChange" :page-size="pageSize" :total="multipleSelection.length">
	    </el-pagination>
	    <el-form :model="dataForm" label-width="auto">
	"""
	for col in columns:
		if ci[col]['type'] in ('many2one','related'):
			s += """
				<el-form-item :label="colsLabel['%s']"
					<el-input v-model="dataForm['%s'].name" :prefix-icon="isCompute('%s') ? 'el-icon-s-data':''" :readonly="readonly('%s')">
						<template #suffix>
							<el-button type="primary" size="mini" icon="el-icon-search" @click="do_find('%s')"/>
							<el-button type="primary" size="mini" icon="el-icon-document-add" @click="do_add('%s')"/>
							<el-button v-if="dataForm['%s'].id != null" type="primary" size="mini" icon="el-icon-edit" @click="do_edit('%s',dataForm['%s'].id)"/></
							<el-button v-if="dataForm['%s'].id != null" type="primary" size="mini" icon="el-icon-view" @click="do_lookup('%s',dataForm['%s'].id)"/>
						</template>
					</el-input>
				</el-form-item>
							""" % (col,col,col,col,col,col,col,col,col,col,col,col)
		elif ci[col]['type'] in ('char','varchar','composite'):
			s += """
				<el-form-item :label="colsLabel['%s']"	
					<el-input v-model="dataForm['%s']" maxlength="%s" show-word-limit :prefix-icon="isCompute('%s') ? 'el-icon-s-data':''" :readonly="readonly('%s')">
						<template #prefix>
						   <el-dropdown v-if="colsTranslate['%s']" @command="i18nCommand">
							  <span class="el-dropdown-link">
								{{colsLang['%s'].toLowerCase()}}<i class="el-icon-arrow-down el-icon--right"></i>
							  </span>
							  <template #dropdown>
								<el-dropdown-menu>
								  <el-dropdown-item v-for="lang in $UserPreferences.langs" :key=lang.code :command="{col:'%s',lang:lang.code}">{{lang.description}}</el-dropdown-item>
								</el-dropdown-menu>
							  </template>
							</el-dropdown>
						 </template>
					</el-input>
				</el-form-item>			
			""" % (col,col,ci[col]['size'] if 'size' in ci[col] and ci[col]['size'] else 2**15-1,col,col,col,col,col)
		elif ci[col]['type'] in ('integer','float','decimal','numeric','timedelta'):
			s += """
				<el-form-item :label="colsLabel['%s']"
					<el-input v-model="dataForm['%s']" :prefix-icon="isCompute('%s') ? 'el-icon-s-data':''" :readonly="readonly('%s')"/>
				</el-form-item>
			""" % (col,col,col,col)
		elif ci[col]['type'] in ('text','xml'):
			s += """
			   	<el-form-item :label="colsLabel['%s']"
					<el-input v-model="dataForm['%s']" type="textarea" :readonly="readonly('%s')"/>            
				</el-form-item>""" % (col,col,col)
		elif ci[col]['type'] == 'json':
			s += """
			   	<el-form-item :label="colsLabel['%s']"
					<json-viewer :value="dataForm['%s']" copyable boxed sort />
				</el-form-item>
				""" % (col,col)
		elif ci[col]['type'] == 'date':
			s += """
			   	<el-form-item :label="colsLabel['%s']"
					<el-date-picker v-model="dataForm['%s']" :readonly="readonly('%s')"/>
				</el-form-item>
				""" % (col,col,col)
		elif ci[col]['type'] == 'time':
			s += """
			   	<el-form-item :label="colsLabel['%s']"
					<el-time-picker v-model="dataForm['%s']" :readonly="readonly('%s')"/>
				</el-form-item>
				""" % (col,col,col)            
		elif ci[col]['type'] == 'datetime':
			s += """
			   	<el-form-item :label="colsLabel['%s']"
					<el-date-picker v-model="dataForm['%s']" type="datetime" :readonly="readonly('%s')"/>            
				</el-form-item>
				""" % (col,col,col)            
		elif ci[col]['type'] == 'selection':
			s += """
			   	<el-form-item :label="colsLabel['%s']"
		            <el-select v-model="dataForm[%s]" :disabled="readonly('%s')">
		                <el-option v-for="item in selOptions['%s']" :key="item.value" :label="item.label" :value="item.value">
		                </el-option>
		            </el-select>
				</el-form-item>
				\n""" % (col,col,col,col)
		elif ci[col]['type'] == 'boolean':
			s += """
			   	<el-form-item :label="colsLabel['%s']"
					<el-checkbox v-model="dataForm['%s']" :disabled="readonly('%s')"/>           
				</el-form-item>
				""" % (col,col,col)	
		elif ci[col]['type'] == 'binary' and ci[col]['accept'] == 'image/*':
			s += """
			   	<el-form-item :label="colsLabel['%s']"
   		            <el-image style="width: 100px; height: 100px" src="https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg" fit="fit"/>
				</el-form-item>
				""" % (col,col,col)

		elif ci[col]['type'] == 'many2many':
			s += """
			   	<el-form-item :label="colsLabel['%s']"
					<gp-m2m-list :metas="metas" :model="metas[model].meta.columns['%s'].obj" :tableData="dataForm['%s']">{{ colsLabel[col] }}</gp-m2m-list>            
				</el-form-item>
				""" % (col,col,col)           

	s += """
		    <el-tabs type="border-card" v-if="o2mcols.length > 0">
		        <el-tab-pane :label="colsLabel[o2mcol]" v-for="o2mcol in o2mcols" :key="o2mcol">
		            <gp-o2m-components :cid="cid" :metas="metas" :model="metas[model].meta.columns[o2mcol].obj" :cdata="dataForm[o2mcol]" :mode="mode"/>
		        </el-tab-pane>
		    </el-tabs>
	    </el-form>
	</slot>
	<slot name="footer">
	    <el-popconfirm confirmButtonText='OK' cancelButtonText='No, Thanks' icon="el-icon-info" iconColor="red" title="Are you sure to cancel?" @confirm="onCancel">
	        <template #reference>
	            <el-button type="danger">Cancel</el-button>
	        </template>
	    </el-popconfirm>
	    <el-button type="success" @click="onValidate">Validate</el-button>
	    <el-button type="primary" @click="onSubmit">Save</el-button>
	</slot>	
</template>		
	"""
	
	print('TEMPLATE:',s)
	return s

def gen_template_el_form_modal(info,columns):
	return """
<template>
	<el-dialog :title="title" v-model="showDialog" width="75%">
	    <el-pagination v-if="oid != null && typeof oid == 'object' && oid.length > 1" background layout="prev, pager, next" @current-change="handleCurrentChange" :page-size="pageSize" :total="oid.length"/>
	    <gp-form :cid="cid" :metas="metas" :model="model"/>
	</el-dialog>
</template>	
	"""

def gen_template_el_list(info,columns):
	return ''

def gen_template_el_m2mlist(info,columns):
	return ''

def gen_template_el_kanban(info,columns):
	return ''

def gen_template_el_tree(info,columns):
	return ''

def gen_template_el_graph(info,columns):
	return ''

def gen_template_el_geo(info,columns):
	return ''
def gen_template_el_calendar(info,columns):
	return ''

def gen_template_el_schedule(info,columns):
	return ''

def gen_template_el_gantt(info,columns):
	return ''

def gen_template_el_mdx(info,columns):
	return ''

def gen_template_el_matrix(info,columns):
	return ''

def gen_template_el_search(info,columns):
	return ''

def gen_template_el_find(info,columns):
	return ''

def gen_template_el_flow(info,columns):
	return ''


gen_template_el = {'form':gen_template_el_form,'form.modal':gen_template_el_form_modal,'list':gen_template_el_list,'m2mlist':gen_template_el_m2mlist,'kanban':gen_template_el_kanban,'tree':gen_template_el_tree,'graph':gen_template_el_graph,'geo':gen_template_el_geo,'calendar':gen_template_el_calendar,'schedule':gen_template_el_schedule,'gantt':gen_template_el_gantt,'mdx':gen_template_el_mdx,'matrix':gen_template_el_matrix,'search':gen_template_el_search,'find':gen_template_el_find,'flow':gen_template_el_flow}

# framework element-plus script
def gen_script_el_form(info,columns):
	return 	standart_gen_script_el_form(info,columns)

def gen_script_el_form_modal(info,columns):
	return ''

def gen_script_el_list(info,columns):
	return ''

def gen_script_el_m2mlist(info,columns):
	return ''

def gen_script_el_kanban(info,columns):
	return ''

def gen_script_el_tree(info,columns):
	return ''

def gen_script_el_graph(info,columns):
	return ''

def gen_script_el_geo(info,columns):
	return ''

def gen_script_el_calendar(info,columns):
	return ''

def gen_script_el_schedule(info,columns):
	return ''

def gen_script_el_gantt(info,columns):
	return ''

def gen_script_el_mdx(info,columns):
	return ''

def gen_script_el_matrix(info,columns):
	return ''

def gen_script_el_search(info,columns):
	return ''

def gen_script_el_find(info,columns):
	return ''

def gen_script_el_flow(info,columns):
	return ''

gen_script_el = {'form':gen_script_el_form,'form.modal':gen_script_el_form_modal,'list':gen_script_el_list,'m2mlist':gen_script_el_m2mlist,'kanban':gen_script_el_kanban,'tree':gen_script_el_tree,'graph':gen_script_el_graph,'geo':gen_script_el_geo,'calendar':gen_script_el_calendar,'schedule':gen_script_el_schedule,'gantt':gen_script_el_gantt,'mdx':gen_script_el_mdx,'matrix':gen_script_el_matrix,'search':gen_script_el_search,'find':gen_script_el_find,'flow':gen_script_el_flow}

# framework element-plus style
def gen_style_el_form(info,columns):
	return standart_gen_empty_scoped_style(info,columns)

def gen_style_el_form_modal(info,columns):
	return standart_gen_empty_scoped_style(info,columns)

def gen_style_el_list(info,columns):
	return standart_gen_empty_scoped_style(info,columns)

def gen_style_el_m2mlist(info,columns):
	return standart_gen_empty_scoped_style(info,columns)

def gen_style_el_kanban(info,columns):
	return standart_gen_empty_scoped_style(info,columns)

def gen_style_el_tree(info,columns):
	return standart_gen_empty_scoped_style(info,columns)

def gen_style_el_graph(info,columns):
	return standart_gen_empty_scoped_style(info,columns)

def gen_style_el_geo(info,columns):
	return standart_gen_empty_scoped_style(info,columns)

def gen_style_el_calendar(info,columns):
	return standart_gen_empty_scoped_style(info,columns)

def gen_style_el_schedule(info,columns):
	return standart_gen_empty_scoped_style(info,columns)

def gen_style_el_gantt(info,columns):
	return standart_gen_empty_scoped_style(info,columns)

def gen_style_el_mdx(info,columns):
	return standart_gen_empty_scoped_style(info,columns)

def gen_style_el_matrix(info,columns):
	return standart_gen_empty_scoped_style(info,columns)

def gen_style_el_search(info,columns):
	return standart_gen_empty_scoped_style(info,columns)

def gen_style_el_find(info,columns):
	return standart_gen_empty_scoped_style(info,columns)

def gen_style_el_flow(info,columns):
	return standart_gen_empty_scoped_style(info,columns)

gen_style_el = {'form':gen_style_el_form,'form.modal':gen_style_el_form_modal,'list':gen_style_el_list,'m2mlist':gen_style_el_m2mlist,'kanban':gen_style_el_kanban,'tree':gen_style_el_tree,'graph':gen_style_el_graph,'geo':gen_style_el_geo,'calendar':gen_style_el_calendar,'schedule':gen_style_el_schedule,'gantt':gen_style_el_gantt,'mdx':gen_style_el_mdx,'matrix':gen_style_el_matrix,'search':gen_style_el_search,'find':gen_style_el_find,'flow':gen_style_el_flow}

# framework vuetify template
def gen_template_vuetify_form(info,columns):
	return ''

def gen_template_vuetify_form_modal(info,columns):
	return ''

def gen_template_vuetify_list(info,columns):
	return ''

def gen_template_vuetify_m2mlist(info,columns):
	return ''

def gen_template_vuetify_kanban(info,columns):
	return ''

def gen_template_vuetify_tree(info,columns):
	return ''

def gen_template_vuetify_graph(info,columns):
	return ''

def gen_template_vuetify_geo(info,columns):
	return ''

def gen_template_vuetify_calendar(info,columns):
	return ''

def gen_template_vuetify_schedule(info,columns):
	return ''

def gen_template_vuetify_gantt(info,columns):
	return ''

def gen_template_vuetify_mdx(info,columns):
	return ''

def gen_template_vuetify_matrix(info,columns):
	return ''

def gen_template_vuetify_search(info,columns):
	return ''

def gen_template_vuetify_find(info,columns):
	return ''

def gen_template_vuetify_flow(info,columns):
	return ''


gen_template_vuetify = {'form':gen_template_vuetify_form,'form.modal':gen_template_vuetify_form_modal,'list':gen_template_vuetify_list,'m2mlist':gen_template_vuetify_m2mlist,'kanban':gen_template_vuetify_kanban,'tree':gen_template_vuetify_tree,'graph':gen_template_vuetify_graph,'geo':gen_template_vuetify_geo,'calendar':gen_template_vuetify_calendar,'schedule':gen_template_vuetify_schedule,'gantt':gen_template_vuetify_gantt,'mdx':gen_template_vuetify_mdx,'matrix':gen_template_vuetify_matrix,'search':gen_template_vuetify_search,'find':gen_template_vuetify_find,'flow':gen_template_vuetify_flow}

# framework vuetify script
def gen_script_vuetify_form(info,columns):
	return ''

def gen_script_vuetify_form_modal(info,columns):
	return ''

def gen_script_vuetify_list(info,columns):
	return ''

def gen_script_vuetify_m2mlist(info,columns):
	return ''

def gen_script_vuetify_kanban(info,columns):
	return ''

def gen_script_vuetify_tree(info,columns):
	return ''

def gen_script_vuetify_graph(info,columns):
	return ''

def gen_script_vuetify_geo(info,columns):
	return ''

def gen_script_vuetify_calendar(info,columns):
	return ''

def gen_script_vuetify_schedule(info,columns):
	return ''

def gen_script_vuetify_gantt(info,columns):
	return ''

def gen_script_vuetify_mdx(info,columns):
	return ''

def gen_script_vuetify_matrix(info,columns):
	return ''

def gen_script_vuetify_search(info,columns):
	return ''

def gen_script_vuetify_find(info,columns):
	return ''

def gen_script_vuetify_flow(info,columns):
	return ''

gen_script_vuetify = {'form':gen_script_vuetify_form,'form.modal':gen_script_vuetify_form_modal,'list':gen_script_vuetify_list,'m2mlist':gen_script_vuetify_m2mlist,'kanban':gen_script_vuetify_kanban,'tree':gen_script_vuetify_tree,'graph':gen_script_vuetify_graph,'geo':gen_script_vuetify_geo,'calendar':gen_script_vuetify_calendar,'schedule':gen_script_vuetify_schedule,'gantt':gen_script_vuetify_gantt,'mdx':gen_script_vuetify_mdx,'matrix':gen_script_vuetify_matrix,'search':gen_script_vuetify_search,'find':gen_script_vuetify_find,'flow':gen_script_vuetify_flow}

# framework vuetify style
def gen_style_vuetify_form(info,columns):
	return ''

def gen_style_vuetify_form_modal(info,columns):
	return ''

def gen_style_vuetify_list(info,columns):
	return ''

def gen_style_vuetify_m2mlist(info,columns):
	return ''

def gen_style_vuetify_kanban(info,columns):
	return ''

def gen_style_vuetify_tree(info,columns):
	return ''

def gen_style_vuetify_graph(info,columns):
	return ''

def gen_style_vuetify_geo(info,columns):
	return ''

def gen_style_vuetify_calendar(info,columns):
	return ''

def gen_style_vuetify_schedule(info,columns):
	return ''

def gen_style_vuetify_gantt(info,columns):
	return ''

def gen_style_vuetify_mdx(info,columns):
	return ''

def gen_style_vuetify_matrix(info,columns):
	return ''

def gen_style_vuetify_search(info,columns):
	return ''

def gen_style_vuetify_find(info,columns):
	return ''

def gen_style_vuetify_flow(info,columns):
	return ''

gen_style_vuetify = {'form':gen_style_vuetify_form,'form.modal':gen_style_vuetify_form_modal,'list':gen_style_vuetify_list,'m2mlist':gen_style_vuetify_m2mlist,'kanban':gen_style_vuetify_kanban,'tree':gen_style_vuetify_tree,'graph':gen_style_vuetify_graph,'geo':gen_style_vuetify_geo,'calendar':gen_style_vuetify_calendar,'schedule':gen_style_vuetify_schedule,'gantt':gen_style_vuetify_gantt,'mdx':gen_style_vuetify_mdx,'matrix':gen_style_vuetify_matrix,'search':gen_style_vuetify_search,'find':gen_style_vuetify_find,'flow':gen_style_vuetify_flow}

# framework devextrme template
def gen_template_devextrme_form(info,columns):
	return ''

def gen_template_devextrme_form_modal(info,columns):
	return ''

def gen_template_devextrme_list(info,columns):
	return ''

def gen_template_devextrme_m2mlist(info,columns):
	return ''

def gen_template_devextrme_kanban(info,columns):
	return ''

def gen_template_devextrme_tree(info,columns):
	return ''

def gen_template_devextrme_graph(info,columns):
	return ''

def gen_template_devextrme_geo(info,columns):
	return ''

def gen_template_devextrme_calendar(info,columns):
	return ''

def gen_template_devextrme_schedule(info,columns):
	return ''

def gen_template_devextrme_gantt(info,columns):
	return ''

def gen_template_devextrme_mdx(info,columns):
	return ''

def gen_template_devextrme_matrix(info,columns):
	return ''

def gen_template_devextrme_search(info,columns):
	return ''

def gen_template_devextrme_find(info,columns):
	return ''

def gen_template_devextrme_flow(info,columns):
	return ''

gen_template_devextrme = {'form':gen_template_devextrme_form,'form.modal':gen_template_devextrme_form_modal,'list':gen_template_devextrme_list,'m2mlist':gen_template_devextrme_m2mlist,'kanban':gen_template_devextrme_kanban,'tree':gen_template_devextrme_tree,'graph':gen_template_devextrme_graph,'geo':gen_template_devextrme_geo,'calendar':gen_template_devextrme_calendar,'schedule':gen_template_devextrme_schedule,'gantt':gen_template_devextrme_gantt,'mdx':gen_template_devextrme_mdx,'matrix':gen_template_devextrme_matrix,'search':gen_template_devextrme_search,'find':gen_template_devextrme_find,'flow':gen_template_devextrme_flow}

# framework devextrme script
def gen_script_devextrme_form(info,columns):
	return ''

def gen_script_devextrme_form_modal(info,columns):
	return ''

def gen_script_devextrme_list(info,columns):
	return ''

def gen_script_devextrme_m2mlist(info,columns):
	return ''

def gen_script_devextrme_kanban(info,columns):
	return ''

def gen_script_devextrme_tree(info,columns):
	return ''

def gen_script_devextrme_graph(info,columns):
	return ''

def gen_script_devextrme_geo(info,columns):
	return ''

def gen_script_devextrme_calendar(info,columns):
	return ''

def gen_script_devextrme_schedule(info,columns):
	return ''

def gen_script_devextrme_gantt(info,columns):
	return ''

def gen_script_devextrme_mdx(info,columns):
	return ''

def gen_script_devextrme_matrix(info,columns):
	return ''

def gen_script_devextrme_search(info,columns):
	return ''

def gen_script_devextrme_find(info,columns):
	return ''

def gen_script_devextrme_flow(info,columns):
	return ''

gen_script_devextrme = {'form':gen_script_devextrme_form,'form.modal':gen_script_devextrme_form_modal,'list':gen_script_devextrme_list,'m2mlist':gen_script_devextrme_m2mlist,'kanban':gen_script_devextrme_kanban,'tree':gen_script_devextrme_tree,'graph':gen_script_devextrme_graph,'geo':gen_script_devextrme_geo,'calendar':gen_script_devextrme_calendar,'schedule':gen_script_devextrme_schedule,'gantt':gen_script_devextrme_gantt,'mdx':gen_script_devextrme_mdx,'matrix':gen_script_devextrme_matrix,'search':gen_script_devextrme_search,'find':gen_script_devextrme_find,'flow':gen_script_devextrme_flow}

# framework devextrme style
def gen_style_devextrme_form(info,columns):
	return ''

def gen_style_devextrme_form_modal(info,columns):
	return ''

def gen_style_devextrme_list(info,columns):
	return ''

def gen_style_devextrme_m2mlist(info,columns):
	return ''

def gen_style_devextrme_kanban(info,columns):
	return ''

def gen_style_devextrme_tree(info,columns):
	return ''

def gen_style_devextrme_graph(info,columns):
	return ''

def gen_style_devextrme_geo(info,columns):
	return ''

def gen_style_devextrme_calendar(info,columns):
	return ''

def gen_style_devextrme_schedule(info,columns):
	return ''

def gen_style_devextrme_gantt(info,columns):
	return ''

def gen_style_devextrme_mdx(info,columns):
	return ''

def gen_style_devextrme_matrix(info,columns):
	return ''

def gen_style_devextrme_search(info,columns):
	return ''

def gen_style_devextrme_find(info,columns):
	return ''

def gen_style_devextrme_flow(info,columns):
	return ''
gen_style_devextrme = {'form':gen_style_devextrme_form,'form.modal':gen_style_devextrme_form_modal,'list':gen_style_devextrme_list,'m2mlist':gen_style_devextrme_m2mlist,'kanban':gen_style_devextrme_kanban,'tree':gen_style_devextrme_tree,'graph':gen_style_devextrme_graph,'geo':gen_style_devextrme_geo,'calendar':gen_style_devextrme_calendar,'schedule':gen_style_devextrme_schedule,'gantt':gen_style_devextrme_gantt,'mdx':gen_style_devextrme_mdx,'matrix':gen_style_devextrme_matrix,'search':gen_style_devextrme_search,'find':gen_style_devextrme_find,'flow':gen_style_devextrme_flow}

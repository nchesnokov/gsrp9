class ORM(object): pass
class INHERIT(object): pass

class BaseModel(ORM): pass
class BaseTrigger(ORM): pass
class BaseReport(ORM): pass
class BaseQuery(ORM): pass
class BaseDialog(ORM): pass
class BaseWizard(ORM): pass
class BaseView(ORM): pass
class BaseDashboard(ORM): pass
class BaseLink(ORM): pass


class BaseModelInherit(INHERIT): pass
class BaseTriggerInherit(INHERIT): pass
class BaseReportInherit(INHERIT): pass
class BaseQueryInherit(INHERIT): pass
class BaseDialogInherit(INHERIT): pass
class BaseWizardInherit(INHERIT): pass
class BaseViewInherit(INHERIT): pass
class BaseDashboardInherit(INHERIT): pass
class BaseLinkInherit(INHERIT): pass


class Model(BaseModel): pass
class Trigger(BaseTrigger): pass
class Report(BaseReport): pass
class Query(BaseQuery): pass
class Dialog(BaseDialog): pass
class Wizard(BaseWizard): pass
class View(BaseView): pass
class Dashboard(BaseDashboard): pass
class Link(BaseLink): pass


class ModelInherit(BaseModelInherit): pass
class TriggerInherit(BaseTriggerInherit): pass
class ReportInherit(BaseReportInherit): pass
class QueryInherit(BaseQueryInherit): pass
class DialogInherit(BaseDialogInherit): pass
class WizardInherit(BaseWizardInherit): pass
class ViewInherit(BaseViewInherit): pass
class DashboardInherit(BaseDashboardInherit): pass
class LinkInherit(BaseLinkInherit): pass

print(issubclass(Report,BaseReport))

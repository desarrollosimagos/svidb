from ajax_select import make_ajax_form,admin
class Autocompletar(admin.AjaxSelectAdmin):
    class Media:
        js=("admin/js/jquery-1.2.6.js","admin/js/jquery.autocomplete.js","admin/js/ajax_select.js")
        css={"all":("admin/css/jquery.autocomplete.css","admin/css/iconic.css")}

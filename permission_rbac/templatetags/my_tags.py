from django import template

register = template.Library()


@register.inclusion_tag("memu.html")
def get_memu(request,):
    memu_permission_list = request.session["memu_permission_list"]
    return {"memu_permission_list": memu_permission_list}

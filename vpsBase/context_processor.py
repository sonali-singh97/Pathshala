from aboutAndStaffs.models import About

def render_footer(request):
    footer_content = About.objects.all()[0]
    return {
        'about_content': footer_content
    }
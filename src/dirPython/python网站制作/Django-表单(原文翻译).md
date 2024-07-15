---
title: Django5.0-表单
---
## HTML表单
在HTML中，表单是`<form>...</form>`内部元素的集合，它允许访问者执行诸如输入文本、选择选项、操作对象或控件等操作，并将这些信息发送回服务器。  
这些表单界面元素中的一些——如文本输入框或复选框——是HTML本身内置的。若要自定义的话则更复杂；往往需要使用前端三剑客来结合实现这些效果。  
除了指定表单元素外，表单还必须指定两件事：  
- 发送到哪里：用户输入对应的数据应该返回到的URL。  
- 如何发送：数据应该通过哪种HTTP方法返回。  
例如，Django管理界面的登录表单包含几个`<input>`元素：一个`type="text"`用于用户名，一个`type="password"`用于密码，以及一个`type="submit"`用于“登录”按钮。它还包含一些用户看不见的隐藏文本字段，Django使用这些字段来确定接下来要执行的操作。  
它还告诉浏览器表单数据应该发送到`<form>`标签的`action`属性中指定的URL——即`/admin/`——并且应该使用`method`属性指定的HTTP机制（`post`）来发送。  
当`<input type="submit" value="Log in">`元素被触发时，数据将被发送回`/admin/`。

## HTTP传送方式：GET和POST
`GET`和`POST`是在处理表单时要使用的两种HTTP方法。  
POST方法用于返回Django的登录表单，其中浏览器将表单数据打包、编码以便传输，发送到服务器，然后接收其响应。  
GET方法将提交的数据捆绑成一个字符串，并使用该字符串构造一个URL。URL包含数据必须发送到的地址，以及数据的键和值。如果你在Django文档中执行搜索，你可以看到这种情况，它会产生一个类似`https://docs.djangoproject.com/search/?q=forms&release=1`的URL。?号后的部分称为查询字符串。  
POST：任何可能用于更改系统状态的请求（例如，在数据库中做出更改的请求）。  
GET：仅应用于不影响系统状态的请求，也不适用于密码表单，因为密码会出现在URL中，因此也会出现在浏览器历史记录和服务器日志中，而且都是明文。它也不适合大量数据或二进制数据（如图像）。  
使用GET请求处理管理表单的Web应用程序存在安全风险：攻击者可以轻松模拟表单请求以访问系统的敏感部分。POST结合Django的CSRF保护等其他保护措施提供了对访问的更多控制。  
另一方面，GET适用于诸如网页搜索表单之类的场景，因为代表GET请求的URL可以轻松地进行书签、共享或重新提交。  

## Django在处理表单方面
处理表单是一项复杂的任务。以Django的admin为例，其中可能需要准备多种不同类型的大量数据以供在表单中显示，将其渲染为HTML，通过方便的界面进行编辑，返回给服务器，进行验证和清理，然后保存或传递给进一步处理。  
Django的表单功能可以简化和自动化这些工作中的大量部分，并且通常比大多数程序员自己编写代码时要安全得多。  
Django处理表单涉及的三个不同部分工作包括：  
1. 准备和重构数据，使其准备好进行渲染
2. 为数据创建HTML表单
3. 接收和处理客户端提交的表单和数据
虽然可以编写代码手动完成所有这些工作，但Django可以为您完成所有这些工作。  

## Django表单
HTML中的`<form>`标签只是表单机制中的一个部分。  
在后端他也可以用Django中的表单类`Form`来代替,与Django中的模型类`Model`描述映射到数据库中的逻辑结构、行为以及组成部分的表示方式非常相似，Form类描述了表单并决定了它的工作方式和外观。  
与模型类的字段映射到数据库字段的方式类似，表单类的字段映射到HTML表单的`<input>`元素。  
(ModelForm即为混合模型与表单类，通过Form将模型类的字段映射到HTML表单的`<input>`元素，让数据库直接与表单进行对接，这也是Django admin管理的基础。)
表单的字段本身也是类；它们管理表单数据并在表单提交时执行验证。DateField和FileField处理非常不同类型的数据，并且需要对这些数据进行不同的操作。  
在浏览器中，表单字段通过HTML“小部件”(widget)呈现给用户——这是一种用户界面机制。每种字段类型都有一个适当的默认Widget类，但可以根据需要进行覆盖。  

### 实例化、处理和渲染表单
在Django中渲染一个对象时，通常遵循以下步骤：  
1. 在视图函数中中获取该对象(例如，从数据库中检索)
2. 将其传递给模板上下文
3. 使用模板变量将其展开为HTML标记  
   
在模板中渲染Form几乎与渲染任何其他类型的对象一样，但存在一些关键差异。  
因此，当我们在视图中处理模型实例时，通常会从数据库中检索它。而当我们处理表单时，我们通常在视图函数中才对其实例化。  
当我们实例化表单时，我们可以选择将其留空或预先填充，例如使用：  
- 从已保存的模型实例中获取的数据(数据库数据上传)
- 我们从其他来源整理的数据(用户自行上传)
- 从之前的HTML表单提交中接收的数据(表单数据转移)
最后一种情况是最有趣的，因为它让用户在能够获取网站数据的基础上，还能够向网站提交修改信息。  

## 创建表单
### 在HTML中指定
最直接的方法就是直接在HTML中编写前端代码，案例如下：  
```html
<form action="/your-name/" method="post">
    <label for="your_name">Your name: </label>
    <input id="your_name" type="text" name="your_name" value="{{ current_name }}">
    <input type="submit" value="OK">
</form>
```
这告诉浏览器使用POST方法将表单数据发送回`/your-name/`URL。它将显示一个文本字段，标签为“Your name:”，以及一个标记为“OK”的按钮。如果模板上下文包含current_name变量，则该变量将用于预先填充your_name字段。  
您需要一个视图来渲染包含HTML表单的模板，并能够根据需要提供`current_name`字段。  
当表单提交时，发送到服务器的POST请求将包含表单数据。  
现在，您还需要一个与`/your-name/`URL相对应的视图，该视图将在请求中找到相应的键值对，然后处理它们。  
直接在HTML中指定表单内容很直观，但在实际应用中，表单可能包含数十个或数百个字段，其中许多字段可能需要预先填充，并且我们可能期望用户在结束操作之前多次经历编辑-提交循环。  
并且我们可能需要在表单提交之前甚至在浏览器中进行一些验证；我们可能想要使用更复杂的字段，允许用户执行诸如从日历中选择日期等操作。  
在这一点上，让Django为我们完成大部分工作要容易得多。  

### Django中指定
因为表单的特殊性，建议在app中定义forms.py文件  
```python
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
```
这定义了一个包含单个字段(your_name)的Form类。我们为字段添加了一个易于理解的标签，该标签在渲染时将出现在`<label>`标签中(尽管在这个例子中，我们指定的标签实际上与如果我们省略它则会自动生成的标签相同)。  
字段的最大允许长度由max_length定义。这有两个作用：首先，它在HTML的`<input>`标签上添加了`maxlength="100"`属性(因此浏览器应首先阻止用户输入超过该数量的字符)。其次，当Django从浏览器接收回表单时，它将验证数据的长度。  
Form实例具有一个`is_valid()`方法，该方法为所有字段运行验证例程。当调用此方法时，如果所有字段都包含有效数据，它将：  
1. 返回True
2. 将表单的数据放置在cleaned_data属性中
当表单首次渲染时，整个表单看起来像这样（HTML结构简化表示）因为不包含form和提交表单，最好是作为模版变量插入html语句中：  
```html
<label for="your_name">Your name: </label>
<input id="your_name" type="text" name="your_name" maxlength="100" required>
```

### 在视图函数：实例化表单
发送到Django网站的表单数据由视图处理，并且通常是发布表单的同一个视图。因此也允许我们重用一些相同的逻辑。  
为了处理表单，我们需要在想要发布表单的URL对应的视图中实例化它：  
```python
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "name.html", {"form": form})
```
如果我们使用GET请求到达这个视图，它会创建一个空的表单实例，并将其放在模板上下文中以进行渲染。这是我们第一次访问该URL时预期会发生的情况。  
如果表单是通过POST请求提交的，视图将再次创建一个表单实例，并用请求中的数据填充它：form = NameForm(request.POST)。这被称为“将数据绑定到表单”（此时它是一个已绑定的表单）。  
我们调用表单的is_valid()方法；如果它不是True，我们将带着表单返回模板。这次，表单不再为空（未绑定），因此HTML表单将被之前提交的数据填充，用户可以根据需要进行编辑和更正。  
如果is_valid()是True，我们现在可以在其cleaned_data属性中找到所有经过验证的表单数据。我们可以使用这些数据来更新数据库或进行其他处理，然后向浏览器发送HTTP重定向，告诉它接下来去哪里，而不是直接显示表单或处理结果。  

### 在模版文件中插入表单
```html
<form action="/your-name/" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit">
</form>
```
因为使用Django后端代替前端实例化了表单，表单类可以当做一个模版变量插入form标签中
:::danger
表单和跨站请求伪造（CSRF）保护  
Django 提供了一种易于使用的跨站请求伪造（CSRF）保护机制。在启用 CSRF 保护的情况下通过 POST 提交表单时，您必须使用如前面示例中所示的 csrf_token 模板标签。然而，由于 CSRF 保护并不直接与模板中的表单相关联，因此在本文档的后续示例中省略了这个标签。
:::
:::danger
HTML5 输入类型和浏览器验证  
如果您的表单包含 URLField、EmailField 或任何整数字段类型，Django 将使用 HTML5 的 url、email 和 number 输入类型。默认情况下，浏览器可能会对这些字段应用自己的验证，这些验证可能比 Django 的验证更严格。如果您想禁用这种行为，可以在表单标签上设置 novalidate 属性，或者为该字段指定不同的控件，如 TextInput。
:::
我们现在有一个工作的Web表单，它由Django表单描述，由视图处理，并渲染为HTML`<form>`。  
这是您开始所需要的全部内容，但表单框架为您提供了更多功能。一旦您理解了上述过程的基本知识，您应该就能够理解表单系统的其他功能，并准备好学习更多关于底层机制的知识。

## 关于Django表单类的更多信息  
所有表单类都是作为django.forms.Form或django.forms.ModelForm的子类创建的。可以将ModelForm视为Form的子类。但它们都从（私有的）BaseForm类继承共同的功能，并不需要关心如何实现其功能
:::danger
模型和表单  
事实上，如果您的表单将直接用于添加或编辑Django模型，ModelForm可以为您节省大量时间、精力和代码，因为它会根据Model类构建表单以及相应的字段和属性。
:::
### 绑定和非绑定表单区分  
区分绑定和非绑定表单很重要：
- 非绑定表单没有与之关联的数据。当呈现给用户时，它将为空或包含默认值。
- 绑定表单具有已提交的数据，因此可用于判断这些数据是否有效。针对无效数据可以包含内联错误消息，告诉用户需要更正哪些数据。
- 表单的is_bound属性将告诉您表单是否有数据与之绑定。

## 更多关于表单的说明
考虑一个比上面最小示例更有用的表单形式，我们可以使用它在个人网站上实现“联系我”的功能：
```python
from django import forms  
  
class ContactForm(forms.Form):  
    subject = forms.CharField(max_length=100)  
    message = forms.CharField(widget=forms.Textarea)  
    sender = forms.EmailField()  
    cc_myself = forms.BooleanField(required=False)
```
我们之前的表单使用了一个单一字段your_name，这是一个CharField。在这个例子中，我们的表单有四个字段：subject、message、sender和cc_myself。CharField、EmailField和BooleanField只是可用的字段类型中的三种；完整的列表可以在表单字段中找到。
### Widgets
每个表单字段都有一个对应的Widget类，该类又对应于HTML表单中的一个小部件，如`<input type="text">`。  
在大多数情况下，字段会有一个合理的默认小部件。例如，默认情况下，CharField会有一个TextInput小部件，它在HTML中生成一个`<input type="text">`。如果你需要`<textarea>`，那么在定义表单字段时，你需要指定对应的Widget值，正如我们对message字段所做的那样。  
### 字段数据
无论通过表单提交了什么数据，一旦它成功通过调用is_valid()方法进行验证（并且is_valid()返回了True），验证后的表单数据将位于form.cleaned_data字典中。这些数据已经被很好地转换成了Python类型。
:::danger
此时，你仍然可以直接从request.POST访问未验证的数据，但验证后的数据更好。在上面的联系表单示例中，cc_myself将是一个布尔值。同样，像IntegerField和FloatField这样的字段分别将值转换为Python的int和float类型。
:::
以下是如何在处理此表单的视图中处理表单数据的方法：  
```python
from django.core.mail import send_mail

# 在视图函数中
if form.is_valid():
    subject = form.cleaned_data["subject"]
    message = form.cleaned_data["message"]
    sender = form.cleaned_data["sender"]
    cc_myself = form.cleaned_data["cc_myself"]

    recipients = ["info@example.com"]
    if cc_myself:
        recipients.append(sender)

    send_mail(subject, message, sender, recipients)
    return HttpResponseRedirect("/thanks/")
```
一些字段类型需要额外的处理。例如，使用表单上传的文件需要不同的处理方式（它们可以从request.FILES中获取，而不是从request.POST）。有关如何使用表单处理文件上传的详细信息，请参阅[]()

## 处理模版中的表单元素
要将表单放入模板中，你所需做的就是将表单实例放入模板的上下文中。因此，如果你在上下文中将表单命名为form，那么`{{ form }}`将会适当地渲染其`<label>`与`<input>`元素。
:::
额外的表单模板元素
不要忘记，表单的输出并不包括周围的`<form>`标签或表单的提交控件。你需要自己提供这些元素。
:::

### 可复用的表单模板
渲染表单时的HTML输出本身是通过模板生成的。你可以通过创建适当的模板文件并设置一个自定义的FORM_RENDERER来在站点范围内使用form_template_name来控制这一点。你还可以通过覆盖表单的template_name属性来自定义每个表单，以使用自定义模板渲染表单，或者将模板名称直接传递给`Form.render()`。
下面的示例将导致`{{ form }}`被渲染为form_snippet.html模板的输出。
```html
<!-- 在模版文件中的形式 -->
{{ form }}
<!-- 最终渲染出的html文件 -->
{% for field in form %}  
    <div class="fieldWrapper">  
        {{ field.errors }}  
        {{ field.label_tag }} {{ field }}  
    </div>  
{% endfor %}
```
然后，你可以在配置文件中配置FORM_RENDERER表单渲染器：  
```python
from django.forms.renderers import TemplatesSetting

class CustomFormRenderer(TemplatesSetting):
    form_template_name = "form_snippet.html"

FORM_RENDERER = "project.settings.CustomFormRenderer"
```


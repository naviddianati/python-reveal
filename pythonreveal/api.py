'''
Created on May 22, 2015
@author: navid

@var dict_kwrds: dict mapping aliases to reveal keywords.
@var dict_classes: dict mapping presentation class name to default CSS class name.
'''

from string import Template
import os


this_dir, this_filename = os.path.split(__file__)
filename_header = os.path.join(this_dir, "header.html")
filename_footer = os.path.join(this_dir, "footer.html")

# Dictionary mapping descriptive keyword name to shorthand
# actually used as function keywords.
dict_kwrds = {
              'data_transition':'trans',
              'background_transition': 'bgtrans',
              'background_color':'background'}

dict_classes = {"Thing":"",
                "Presentation":"",
                "Tag":"",
                "Header":"header",
                "Column":"column",
                "Row":"row",
                "Paragraph":"paragraph",
                "Image":"image",
                "Page":"page",
                "PageSection":"pagesection",
                "FrontPage":"frontpage",
                "H1":"",
                "H2":"",
                "H3":"",
                "H4":"",
                "Vspace":"vspace",
                "Video":"",
                "Author":"author",
                "Institution":"institution",
                "EndPage":"endpage",
                'List' : 'list',
                'ListItem':'listitem',
                'Link':'link'
                }



class Config():
    '''
    @deprecated: Use L{Theme} instances instead.
    '''
    def __init__(self):
        self.defaults = {'data_transition': 'linear',
                         'background_transition':'slide',
                         'background_color':''}

config = Config()


class Theme():
    '''
    Class containing CSS options.
    @ivar raw_css: string of raw css code prepended to the
    compiled CSS.
    @ivar dict_css: dict mapping CSS selector to a dict of
    attribute, values.
    '''
    def __init__(self):

        self.raw_css = ''
        self.dict_css = {}
        self.dict_css['.reveal'] = {'font-family':'Calibri', 'font-weight':'bold',
                                    'font-size':'46px', 'letter-spacing': '-0.02em',
                                    'text-transform':'none'}
        self.dict_css['.reveal h1'] = {}
        self.dict_css['.reveal h2'] = {}
        self.dict_css['.reveal h3'] = {}
        self.dict_css['.reveal h4'] = {}
        self.dict_css['.reveal p'] = {}
        self.dict_css['.reveal a'] = {}
        self.dict_css['.reveal li'] = {'font-size':'1em'}
        self.dict_css['.reveal li li'] = {'font-weight':'normal', 'font-size':'0.9em', 'margin-left': '1em'}
        self.dict_css['.reveal li ul'] = {'font-weight':'normal', 'font-size':'0.9em', 'margin-left': '1em'}
        self.dict_css['.reveal ul li'] = {'font-weight':'normal', 'font-size':'0.9em', 'margin-left': '1em'}
        self.dict_css['.reveal ul ul'] = {'font-weight':'normal', 'font-size':'0.9em', 'margin-left': '1em'}
        self.dict_css['.reveal ul, .reveal ol'] = {'text-align':'left', 'display':'block'}
        self.dict_css['.reveal b'] = {}
        self.dict_css['.reveal em'] = {}

        self.dict_css['.reveal .column'] = { 'font-weight':'bold'}
        self.dict_css['.reveal .row'] = {'margin-bottom':'10px', 'font-weight':'bold', 'clear':'left'}
        self.css('.reveal .row', {"display": "flex", "flex-flow": "row nowrap", "align-items": "flex-end"})
        self.dict_css['.reveal .row.top'] = {'align-items':'flex-start'}
        self.dict_css['.reveal .row.middle'] = {'align-items':'center'}
        self.dict_css['.reveal .row.bottom'] = {'align-items':'flex-end'}
        self.dict_css['.reveal .paragraph'] = {}
        self.dict_css['.reveal .image'] = {}
        self.dict_css['.reveal .paragraph'] = {'font-weight':'bold'}
        self.dict_css['.reveal .page'] = {'top': '0%', 'height':'100%'}
        self.dict_css['.reveal .pagesection'] = {'height':'100%'}
        self.dict_css['.reveal .frontpage'] = {}
        self.dict_css['.reveal h2.vspace'] = {'margin':'0px'}
        self.dict_css['.reveal sup'] = {'font-size':'0.5em', 'color':'#eee', 'margin':'0.3em', 'font-weight':'lighter'}
        self.dict_css['.author'] = {}
        self.dict_css['.institution'] = {}

        # Misc classes
        self.css('.reveal .textshadow-large', {"text-shadow": "5px 5px 15px #111"})
        self.css('.reveal .textshadow-small', {"text-shadow": "5px 5px 5px #111"})
        self.css('.reveal .textshadow-center', {"text-shadow": "0px 0px 3px #111"})
        self.css('.reveal .h2yellow', {'color': '#FFD800', 'margin': '0.5empx',
                                       'line-height': '0.8em', 'font-weight':' bold',
                                       'font-size':' 2em', 'text-shadow':' 5px 5px 5px #222'})
        self.css('.reveal .email', {'font-family':'Calibri'})

        self.css('.align-center > *', {'margin-right':'auto', 'margin-left':'auto'})
        self.css('.reveal .reference, .reveal li.reference', {'font-family':'Computer Modern Serif', 'color': '#333',
                                  'font-size': '0.7em', 'line-height': '1.3',
                                  'letter-spacing': '0.00em', 'font-weight': 'normal'})


        self.define()

    def define(self):
        '''
        Override to personalize the theme.
        '''

        self.css('.reveal', {'font-family':'Calibri', 'font-weight':'bold', 'font-size':'46px', 'letter-spacing': '-0.02em'})
        self.css(['.reveal h2', '.reveal h3', '.reveal h4'],
                 {'margin':'0 0 1em 0', 'font-family':'Lato', 'line-height':'1em',
                  'letter-spacing':'-0.01em', 'text-transform':'none'})

        self.css(['.reveal h2', '.reveal h3', '.reveal h4', '.reveal p'], {'width':'100%'})
        self.css('.reveal h2', {'font-size':'1.5em', 'font-weight':'bold'})
        self.css('.reveal h3', {'font-size':'1em'})
        self.css('.reveal h4', {'font-size':'1em'})
        self.css('.reveal h4.author', {'font-family':'Lato', 'color':'#FFD800', 'margin':'0.3em'})
        self.css('.reveal h4.institution', {'font-family':'Lato', 'font-weight':'100', 'color':'#ddd', 'margin-bottom':'0.5em'})
        self.css('.reveal p', {'text-align':'justify', 'color':'#eee'})
        self.css(['.reveal .image', '.reveal .video'], {"box-shadow" : "15px 15px 20px #222;", 'border':'solid thin #222'})

        self.css('.reveal h2.header', {'color':'#FFD700',
#                                        'border-bottom':'solid thin #ddd','border-top':'solid thin #ddd',
                                       'padding-bottom':'0.5em', 'padding-top':'0.5em',
                                       'margin-bottom':'0.5em'})

        # Text shaddow
        self.css(['h2.title', 'h4.author', 'h2.header'], {"text-shadow": "5px 5px 20px #222"})
        self.css(['.reveal b', '.reveal em'], {"text-shadow": "0px 0px 10px #111"})
        self.css('.reveal b', {'color':'#9999FF'})

        self.css('.reveal h2.vertical-center', {'position': 'relative',
                                              '-webkit-transform': r'translateY(-80%)',
                                              '-moz-transform': 'translateY(-50%)'})

        self.css('.reveal .pagesection h2', {'font-size':'2em', "text-shadow": "5px 5px 15px #111"})
        self.css('.reveal p.paragraph', {'font-family':'Calibri', 'font-weight':'bold', "text-shadow": "0px 0px 10px #111"})

    def css(self, selectors, rules):
        '''
        Update or add CSS attributes.
        @param selectors: the selector(s) to add/update. Can be
        a string or a list of strings which will be concatenated.
        @param rules: dict of CSS attribute:value pairs.
        '''
        if type(selectors) == str:
            try:
                self.dict_css[selectors].update(rules)
            except KeyError:
                self.dict_css[selectors] = rules
        elif type(selectors) == list:
            try:
                self.dict_css[','.join(selectors)].update(rules)
            except:
                self.dict_css[','.join(selectors)] = rules





    def export_css(self):
        '''
        Compile all CSS rules to string.
        '''
        s = self.raw_css
        for selector, code in self.dict_css.iteritems():
#             print selector,code
            s += "%s{\n" % selector
            for key, value in code.iteritems():
                if not key: continue
                s += "    %s : %s;\n" % (key, value)
            s += "}\n\n"
        return s
    def export_style(self):
        '''
        surround the compiled CSS code with <style></style>
        tags. To be placed in the header of the html file.
        '''
        s = '\n<style>\n%s\n</style>\n' % self.export_css()
        return s


class ThemeDark(Theme):
    def __init__(self):
        Theme.__init__(self)
        pass
        self.dict_css = {}

class ThemeDark(Theme):
    def __init__(self):
        self.dict_css = {}
        Theme.__init__(self)
        pass

    def define(self):
        '''
        Override to personalize the theme.
        '''
#         self.css('body',{'background':'#202020'})
        self.css(['.reveal .present>.page-wrapper'],
                 {
#                   'display':'flex !important','flex-flow':'column',
                  'height':'95%'})
        self.css('.reveal', {'font-family':'Calibri', 'font-weight':'bold', 'font-size':'46px', 'letter-spacing': '-0.02em'})
        self.css(['.reveal h2', '.reveal h3', '.reveal h4'],
                 {'margin':'0 0 0.5em 0', 'font-family':'Lato', 'line-height':'1em',
                  'letter-spacing':'-0.01em', 'text-transform':'none'})

        self.css(['.reveal h2', '.reveal h3', '.reveal h4', '.reveal p'], {'width':'100%'})
        self.css('.reveal h2', {'font-size':'1.5em', 'font-weight':'bold'})
        self.css('.reveal h3', {'font-size':'1em'})
        self.css('.reveal h4', {'font-size':'1em'})
        self.css('.reveal h4.author', {'font-family':'Lato', 'color':'#FFD800', 'margin':'0.3em'})
        self.css('.reveal h4.institution', {'font-family':'Lato', 'font-weight':'100', 'color':'#ddd', 'margin-bottom':'0.5em', 'font-size':'0.8em'})
        self.css('.reveal p', {'text-align':'justify', 'color':'#eee'})
        self.css(['.reveal .image', '.reveal .video'],
                  {"box-shadow" : "15px 15px 20px #222;", 'border':'solid thin #222',
                   'border-radius': '10px'})

        self.css('.reveal h2.header', {'color': '#fff',  # 97FFA7', #FFD700',
#                                        'border-bottom':'solid thin #ddd','border-top':'solid thin #ddd',
                                       'padding-bottom':'0.5em', 'padding-top':'0.5em',
                                       'margin-bottom':'0.5em'})

        # Text shaddow
        self.css(['h2.title', 'h4.author', 'h2.header', '.reveal h2', '.reveal h3', '.reveal h4'], {"text-shadow": "5px 5px 20px #222"})
        self.css(['.reveal b', '.reveal em'], {"text-shadow": "0px 0px 5px #111"})
#         self.css(['.reveal b', '.reveal em'], {"text-shadow": "none"})
#         self.css('.reveal b', {'color':'#9999FF'})
        self.css('.reveal b', {'color':'#F5EE31'})

        self.css('.reveal h2.vertical-center', {'position': 'relative',
                                              '-webkit-transform': r'translateY(-80%)',
                                              '-moz-transform': 'translateY(-50%)'})

        self.css('.reveal .pagesection h2', {'font-size':'2em', "text-shadow": "5px 5px 15px #111", 'font-weight':'lighter'})
        self.css('.reveal p.paragraph', {'font-family':'Calibri', 'font-weight':'bold', "text-shadow": "0px 0px 10px #111"})
        self.css('.reveal li.reference, .reveal .reference', {'color': '#ddd', })
        self.css('.reveal img.white', {"background":"white", 'padding':'0.5em', 'border': 'solid 3px #333',
                                      'margin-right':'0.5em', 'margin-left':'0.5em'})
        self.css('.reveal img.black', {"background":"black", 'padding':'0.5em', 'border': 'solid 3px #9999FF',
                                      'margin-right':'0.5em', 'margin-left':'0.5em'})

        # MathJax
        self.css('.reveal .MathJax_SVG', {'color':'#fff'})

        # lists
        self.css('.reveal ol li', {'color':'#9999FF'})
        self.css('.reveal ul li', {'color':'#9999FF'})
        self.css('.reveal ol li span', {'color':'#ddd'})
        self.css('.reveal ul li span', {'color':'#ddd'})

        # Custom classes
        self.css('.reveal .h2yellow', {'font-family':'Calibri'})
        self.css('.reveal p.paragraph.normalweight', {'font-weight':'lighter'})






class Tag():
    '''
    Abstract class representing a generic HTML tag.
    @ivar html_template: list of length 3.
    @ivar attributes: set of html attribute tuples. Will be inserted
    into the opening tag as C{attribute="value"}.
    '''
    def __init__(self, **kwargs):
        '''
        @keyword dict_css: a dict of CSS properties.
        @keyword classes: list of css classes.
        @keyword tag: optional tage string.
        @keyword background: CSS background property.
        @keyword color: CSS font color.
        @keyword align: CSS text-align property.

        '''
        self.raw_css = ''
        self.dict_css = kwargs.get('dict_css', {})
        self.classes = kwargs.get('classes', [])
        self.tag = kwargs.get('tag', 'div')
        self.html_template = ['<' + self.tag + ' %s>', '', '</' + self.tag + '>']

        color = kwargs.get('color')
        align = kwargs.get('align')
        background = kwargs.get('background')

        self.color(color)
        self.align(align)
        self.background(background)
        self.attributes = set()

    def setDefaultClass(self):
        '''
        Add the default CSS class of the specific tag type.
        '''
        name = self.__class__.__name__
        self.classes.append(dict_classes[name])

    def css(self, input):
        '''
        Add or update the CSS dict.
        @param input: a tuple or dict containing CSS key,values. If a tuple,
        the tuple will be interpreted as (key,value). Multiple attributes can
        be set using a dict.
        '''
        if type(input) == dict:
            for key, value in input.iteritems():
                self.dict_css[key] = value
        elif type(input) == tuple:
            self.dict_css[input[0]] = input[1]
        elif type(input) == str:
            self.raw_css += str
        return self

    def getCSS(self):
        '''
        Return the string for the inline CSS styling of the
        tag: " class='...'"
        '''
        s = self.raw_css
        if self.dict_css:
            for key, value in self.dict_css.iteritems():
                s += "%s:%s; " % (key, value)

            output = ' style="%s"'
            return output % s
        else:
            return ''

    def add_attribute(self, attribute, value):
        '''
        Add an HTML attribute to tag.
        '''
        self.attributes.add((attribute, value))


    def getHTMLOptions(self):
        '''
        Return a string containing the "class" tag options.
        '''
        s = ''
        if self.classes:
            s += ' class="%s" ' % " ".join(self.classes)
        if self.attributes:
            s += ' '.join(['%s="%s"' % (attr, value) for attr, value in self.attributes])
        s += self.getCSS()
        return s


    def color(self, color):
        '''
        Set the text color of the tag.
        @param color: CSS color string.
        @return: the current tag.
        '''
        if color: self.css({'color': color})
        return self
    def align(self, align):
        '''
        Set the text-align of the tag.
        @param align: CSS text-align string.
        @return: the current tag.
        '''
        if align: self.css({'text-align':align})
        return self
    def center(self):
        self.align('center')
        return self

    def background(self, background):
        '''
        Set the background color of the tag.
        @param background: CSS background string.
        @return: the current tag.
        '''
        if background: self.css({'background':background})
        return self

    def fontsize(self, fontsize):
        '''
        Set the font-size of the tag.
        @param fontsize: CSS font-size string.
        @return: the current tag.
        '''
        if fontsize: self.css({'font-size':fontsize})
        return self

    def font(self, family='', weight='', size=''):
        '''
        Set the font family and font weight of the tag.
        @param family: CSS font-family string.
        @param weight: CSS font-weight string.
        @param size: CSS font-size string.
        @return: the current tag.
        '''
        if family: self.css({'font-family':"'%s'" % family})
        if weight: self.css({'font-weight':str(weight)})
        if size: return self.fontsize(size)

        return self

    def cl(self, classname):
        '''
        Add a CSS class to the tag.
        @param classname: CSS class name.
        @return: the current tag.
        '''
        self.classes.append(classname)
        return self

    def margin(self, margin):
        '''
        Set the CSS margin of the element.
        @param margin: CSS margin.
        @return: the curent tag.
        '''
        self.css({'margin':margin})
        return self

    def padding(self, padding):
        '''
        Set the CSS padding of the element.
        @param padding: CSS padding.
        @return: the curent tag.
        '''
        self.css({'padding':padding})
        return self

class Floater(Tag):
    '''
    Abstract class with CSS floating properties and methods.
    '''
    def __init__(self, **kwargs):
        Tag.__init__(self, **kwargs)
        pass
    def left(self):
        '''
        Set CSS C{float} to C{left}
        '''
        self.css(('float', 'left'))
        return self
    def right(self):
        '''
        Set CSS C{float} to C{right}
        '''
        self.css(('float', 'right'))
        return self




class Shape(Tag):
    '''
    Abstract class with geometric properties: width, height.
    '''
    def __init__(self, **kwargs):
        '''
        @keyword w: width.
        @keyword h: height.
        '''
        Tag.__init__(self, **kwargs)
        self.attr_width = kwargs.get('w', '')
        self.attr_height = kwargs.get('h', '')
        if self.attr_width:
            self.dict_css(("width", self.attr_width))
        if self.attr_height:
            self.css(("height", self.attr_height))

    def width(self, width):
        '''
        Set the CSS width property.
        @param width: CSS width string.
        @return: current object.
        '''
        self.css(("width", width))
        return self
    def w(self, width):
        '''
        Alias for L{self.width}
        '''
        return self.width(width)

    def height(self, height):
        '''
        Set the CSS height property.
        @param height: CSS height string.
        @return: current object.
        '''
        self.css(("height", height))
        return self
    def h(self, height):
        '''
        Alias for L{self.height}
        '''
        return self.height(height)






class Thing(Floater, Shape):
    '''
    Base class for all objects in a presentation: page,
    column, paragraph, etc.
    @ivar parent: the parent object.
    @ivar children: list of child objects.
    @ivar Columns: list of child columns.
    @ivar Paragraphs: list of child paragraphs
    @todo: is L{Paragraphs} used at all?
    @ivar Rows: list of child rows.
    @ivar Images: list of child images.
    @ivar Pages: list of child pages.
    '''
    def __init__(self, **kwargs):
        '''
        @see: L{Tag}, L{Shape}, L{Floater} for keyword arguments.
        '''
        Floater.__init__(self, **kwargs)
        Shape.__init__(self, **kwargs)
        self.setDefaultClass()

        self.children = []
        self.parent = None
        self.Columns = []
        self.Paragraphs = []
        self.Images = []
        self.Rows = []
        self.Pages = []

        self.presentation = None

        self.html_template = ["<div%s>", "", "</div>"]


    def div(self, **kwargs):
        '''
        Add a generic L{Thing} to children and return it.
        '''
        x = Thing(**kwargs)
        self.add(x)
        return x


    def add(self, something):
        '''
        Add a child object to the current object. If the child
        is a Column, Row, Paragraph, Image or Page, add it to the
        specific corresponding list as well.
        '''
        assert issubclass(something.__class__, Tag)
        if something.__class__.__name__ == "Column":
            self.Columns.append(something)
        elif something.__class__.__name__ == "Row":
            self.Rows.append(something)
        elif something.__class__.__name__ == "Paragraph":
            self.Paragraphs.append(something)
        elif something.__class__.__name__ == "Image":
            self.Images.append(something)
        elif something.__class__.__name__ == "Page":
            self.Pages.append(something)

        self.children.append(something)
        something.parent = self


    def get_presentation(self):
        if isinstance(self, Presentation):
            return self
        else:
#             print self
            return self.parent.get_presentation()

    def dig(self):
        '''
        Recursively compile the html code for the object
        and all its children.
        @return: the html code for the object and all its
        decendants.
        '''
        s = []
        for c in self.children:
            s += ["    %s" % x for x in c.dig()]
        try:
            result = [self.html_template[0] % self.getHTMLOptions()] + s + [self.html_template[2]]
        except:
            print self.html_template[0]
#             print s
            raise
        return result


    def fr(self, order=None):
        '''
        Hide theh object initially. It will appear after
        the move-forward key stroke.
        Add the C{fragment} class to the object
        @return: self.
        '''
        if order:
            self.add_attribute('data-fragment-index', '%d' % order)
        self.cl('fragment')
        return self

    def vspace(self, h='1em', **kwargs):
        '''
        Add a Vspace.
        '''
        x = Vspace(h)
        self.add(x)
        return x

    def addList(self, ordered=False, **kwargs):
        '''
        Create and add a new html list as a child.
        '''
        x = List(ordered, **kwargs)
        self.add(x)
        return x
    def ulist(self, **kwargs):
        '''
        Add unordered list.
        '''
        return self.addList(ordered=False, **kwargs)
    def ul(self, **kwargs):
        '''
        Alias for L{self.ulist}
        '''
        return self.ulist(**kwargs)
    def olist(self, **kwargs):
        '''
        Add ordered list.
        '''
        return self.addList(ordered=True, **kwargs)
    def ol(self, **kwargs):
        '''
        Alias for L{self.olist}
        '''
        return self.olist(**kwargs)


    def addParagraph(self, html='', **kwargs):
        '''
        Create and add a new paragraph object as a child.
        @param html: the html code to go inside the paragraph.
        @return: the newly created L{Paragraph} object.
        '''
        x = Paragraph(html=html, **kwargs)
        self.add(x)
        return x
    def par(self, html, **kwargs):
        '''
        Alias for L{addParagraph}.
        '''
        return self.addParagraph(html=html, **kwargs)


    def addH1(self, html='', **kwargs):
        '''
        Create and add a new H1 object as a child.
        @param html: the html code to go inside the H1.
        @return: the newly created L{H1} object.
        '''
        x = H1(html=html, **kwargs)
        self.add(x)
        return x
    def h1(self, html, **kwargs):
        '''
        Alias for L{addH1}
        '''
        return self.addH1(html=html, **kwargs)


    def addH2(self, html='', **kwargs):
        '''
        Create and add a new H2 object as a child.
        @param html: the html code to go inside the H2.
        @return: the newly created L{H2} object.
        '''
        x = H2(html=html, **kwargs)
        self.add(x)
        return x
    def h2(self, html, **kwargs):
        '''
        Alias for L{addH2}
        '''
        return self.addH2(html=html, **kwargs)


    def addH3(self, html='', **kwargs):
        '''
        Create and add a new H3 object as a child.
        @param html: the html code to go inside the H3.
        @return: the newly created L{H3} object.
        '''
        x = H3(html=html, **kwargs)
        self.add(x)
        return x
    def h3(self, html, **kwargs):
        '''
        Alias for L{addH3}
        '''
        return self.addH3(html=html, **kwargs)


    def addH4(self, html='', **kwargs):
        '''
        Create and add a new H4 object as a child.
        @param html: the html code to go inside the H4.
        @return: the newly created L{H4} object.
        '''
        x = H4(html=html, **kwargs)
        self.add(x)
        return x
    def h4(self, html, **kwargs):
        '''
        Alias for L{addH4}
        '''
        return self.addH4(html=html, **kwargs)

    def addImage(self, src, **kwargs):
        '''
        Create and add a new Image object as a child.
        @param src: the C{src} source of the image.
        @return: the newly created L{Image} object.
        '''
        x = Image(src=src, **kwargs)
        self.add(x)
        return x
    def im(self, src, **kwargs):
        '''
        Alias for L{addImage}
        '''
        return self.addImage(src, **kwargs)


    def addVideo(self, src, **kwargs):
        '''
        Create and add a new Video object as a child.
        @param src: the C{src} source of the Video.
        @return: the newly created L{Video} object.
        '''
        x = Video(src=src, **kwargs)
        self.add(x)
        return x
    def video(self, src, **kwargs):
        '''
        Alias for L{addVideo}
        '''
        return self.addVideo(src, **kwargs)

    def addLink(self, url, text, **kwargs):
        x = Link(url,text, **kwargs)
        self.add(x)
        return x
    def link(self,url, text, **kwargs):
        return self.addLink(url,text, **kwargs)



    def addRow(self, tid, **kwargs):
        '''
        Create and add a new L{Row} child object if L{tid}
        is new, otherwise return the existing Row with id C{tid}.
        @param tid: the integer id of the Row to retrieve
        or create.
        @return: the retrieved or newly created L{Row} object.
        '''
        try:
            return self.Rows[tid - 1]
        except IndexError:
            x = Row(**kwargs)
            self.add(x)
            return x
    def i(self, tid=0, **kwargs):
        '''
        Alias for L{addRow}
        '''
        return self.addRow(tid, **kwargs)
    def r(self, tid=0, **kwargs):
        '''
        Alias for L{addRow}
        '''
        return self.addRow(tid, **kwargs)



    def addColumn(self, tid, **kwargs):
        '''
        Create and add a new L{Column} child object if L{tid}
        is new, otherwise return the existing Column with id C{tid}.
        @param tid: the integer id of the column to retrieve
        or create.
        @return: the retrieved or newly created L{Column} object.
        '''
        try:
            return self.Columns[tid - 1]
        except IndexError:
            x = Column(**kwargs)
            self.add(x)
            return x
    def j(self, tid=0, **kwargs):
        '''
        Alias for L{addColumn}
        '''
        return self.addColumn(tid, **kwargs)
    def c(self, tid=0, **kwargs):
        '''
        Alias for L{addColumn}
        '''
        return self.addColumn(tid, **kwargs)




class Link(Thing):
    def __init__(self, url='', text='', **kwargs):
        '''
        @param url: url code to go inside the tag.
        '''
        Thing.__init__(self, **kwargs)
        self.html_template = ["<a %s href='{url}' target='_blank'>".format(url=url), "", "</a>"]
        self.text = text
    def dig(self):
        return [self.html_template[0] % self.getHTMLOptions(), self.text, self.html_template[2]]



class Text(Thing):
    '''
    Generic text tag. Can be subclassed to create
    C{h1}, C{h2}, C{p}, etc.
    '''
    def __init__(self, html, **kwargs):
        '''
        @param html: html code to go inside the tag.
        '''
        Thing.__init__(self, **kwargs)
        self.html = html
    def dig(self):
        return [self.html_template[0] % self.getHTMLOptions(), self.html, self.html_template[2]]

class H1(Text):
    '''
    Class representing an html C{h1} tag.
    '''
    def __init__(self, html='', **kwargs):
        '''
        @param html: html code to go inside the tag.
        '''
        Text.__init__(self, html, **kwargs)
        self.html_template = ["<h1%s>", "", "</h1>"]

class H2(Text):
    '''
    Class representing an html C{h1} tag.
    '''
    def __init__(self, html='', **kwargs):
        '''
        @param html: html code to go inside the tag.
        '''
        Text.__init__(self, html, **kwargs)
        self.html_template = ["<h2%s>", "", "</h2>"]

class H3(Text):
    '''
    Class representing an html C{h1} tag.
    '''
    def __init__(self, html='', **kwargs):
        '''
        @param html: html code to go inside the tag.
        '''
        Text.__init__(self, html, **kwargs)
        self.html_template = ["<h3%s>", "", "</h3>"]

class H4(Text):
    '''
    Class representing an html C{h1} tag.
    '''
    def __init__(self, html='', **kwargs):
        '''
        @param html: html code to go inside the tag.
        '''
        Text.__init__(self, html, **kwargs)
        self.html_template = ["<h4%s>", "", "</h4>"]

class Paragraph(Text):
    '''
    Class representing an html C{h1} tag.
    '''
    def __init__(self, html='', **kwargs):
        '''
        @param html: html code to go inside the tag.
        '''
        Text.__init__(self, html, **kwargs)
        self.html_template = ["<p%s>", "", "</p>"]



class Image(Thing):
    '''
    Class representing an html C{img} tag. If this instance is bound to
    a L{Presentation} instance and the presentation's C{data_dir} is set,
    then the C{src} parameter is prepended by that url.
    '''
    def __init__(self, src='', **kwargs):
        '''
        @param src: src url of the image.
        '''
        Thing.__init__(self, **kwargs)
        self.html_template = ["<img%s>", "", "</img>"]
        self.src = src

    def dig(self):
        return [self.html_template[0] % self.getHTMLOptions(), '', self.html_template[2]]

    def getHTMLOptions(self):
        s = Thing.getHTMLOptions(self)
        # Prepend by the presentation's data_dir if set.
        presentation = self.get_presentation()
#         print presentation
        src = self.src
        if src[0] in ['.', '/'] or src[:4] == 'http' or src[:3] == 'www':
            pass
        else:
            src = (presentation.data_dir or "") + self.src

        if src:
            s += ' src="%s" ' % src
        return s

class Video(Thing):
    '''
    Class representing an html C{video} tag.
    '''
    def __init__(self, src='', **kwargs):
        '''
        @param src: src url of the image.
        '''
        Thing.__init__(self, **kwargs)

        loop = kwargs.get('loop', False)
        autoplay = kwargs.get('autoplay', False)

        loop = 'loop' if loop else ''
        autoplay = 'autoplay' if autoplay else ''

        self.html_template = ['<video%s controls {loop} {autoplay}>\
        <source  type="video/mp4">'.format(loop=loop, autoplay=autoplay), "</video>"]
        self.src = src
    def dig(self):
        return [self.html_template[0] % self.getHTMLOptions(), '', self.html_template[1]]

    def getHTMLOptions(self):
        s = Thing.getHTMLOptions(self)
        if self.width:
            s + ' width="%s"' % self.width
        if self.height:
            s + ' height="%s"' % self.height

        # Prepend by the presentation's data_dir if set.
        presentation = self.get_presentation()
        src = self.src
        if src[0] in ['.', '/'] or src[:4] == 'http' or src[:3] == 'www':
            pass
        else:
            src = (presentation.data_dir or "") + self.src

        if src:
            s += ' src="%s" ' % src
        return s



class Page(Thing):
    '''
    Class representing a page in the presentation.
    '''
    def __init__(self, header='', **kwargs):
        '''
        @keyword data_transition: the reveal C{data_transition} attribute.
        @keyword background_color: the reveal C{data-background} color attribute.
        @keyword background_transition: the reveal C{data-background-transition} attribute.
        '''
        Thing.__init__(self, **kwargs)
        self.transition = kwargs.get(dict_kwrds['data_transition'], config.defaults['data_transition'])
        self.background = kwargs.get(dict_kwrds['background_color'], config.defaults['background_color'])
        self.background_transition = kwargs.get(dict_kwrds['background_transition'], config.defaults['background_transition'])
        self.header(header)
        self.html_template = ["<section%s>", "", "</section>"]

    def getHTMLOptions(self):
        s = Thing.getHTMLOptions(self)
        if self.transition:
            s += ' data-transition="%s" ' % self.transition
        if self.background_transition:
            s += ' data-background-transition="%s" ' % self.background_transition
        if self.background:
            s += ' data-background="%s" ' % self.background
        return s
    def header(self, text=''):
        '''
        Set the header of the page.
        @param text: the header text.
        '''
        h = None
        if text:
            h = self.h2(text).cl('header').color(self.dict_css.get('color'))
        return h


class PageSection(Page):
    '''
    Class for transition pages. This page contains one
    vertically and horizontally centered text tag.
    '''
    def __init__(self, html, **kwargs):
        '''
        @param html: the html code to go into the centered text tag.
        '''
        Page.__init__(self, **kwargs)
        self.transition = "zoom"
        self.background = "#333"
        self.cl("section-centered")
        self.html_template = ["<section%s>", "", "</section>"]
        self.add(Vspace('50%'))
        self.addH2(html).color('#fff').classes = ['white', 'vertical-center', 'newsection']


class List(Thing):
    '''
    Class for an html list C{ul} tag.
    '''
    def __init__(self, ordered=False, **kwargs):
        Thing.__init__(self)
        if ordered:
            self.html_template = ["<ol%s>", "", "</ol>"]
        else:
            self.html_template = ["<ul%s>", "", "</ul>"]
    def item(self, text):
        '''
        Create and add a list item child object with the
        given text.
        @param text: the text of the chlid list item object.
        '''
        l = ListItem(text)
        self.add(l)
        return l

class ListItem(Thing):
    '''
    Class for an html list item C{li} tag.
    '''
    def __init__(self, html='', **kwargs):
        '''
        @param html: html code to go inside the C{li} tag.
        '''
        Thing.__init__(self)
        self.html = html
        self.html_template = ["<li%s><span>", "", "    </span></li>"]
    def dig(self):
        s = []
        for c in self.children:
            s += ["    %s" % x for x in c.dig()]
        result = [self.html_template[0] % self.getHTMLOptions()] + [self.html] + s + [self.html_template[2]]
        return result

class Header(Thing):
    def __init__(self, **kwargs):
        Thing.__init__(self)
        self.html_template = ["<h1%s>", "", "</h1>"]


class Row(Thing):
    '''
    Class for a row in the page.
    '''
    def __init__(self, **kwargs):
        Thing.__init__(self, **kwargs)
        self.html_template = ["<div%s>", "", "</div>"]
    def top(self):
        '''
        Make the contents top-aligned
        '''
        self.cl('top')
        return self

    def middle(self):
        '''
        Make the contents middle-aligned
        '''
        self.cl('middle')
        return self

    def bottom(self):
        '''
        Make the contents bottom-aligned
        '''
        self.cl('bottom')
        return self

class Column(Thing):
    '''
    Class for a column object in the page.
    '''
    def __init__(self, **kwargs):
        Thing.__init__(self, h="100%", css={"display":"block", "text-align":"left"})
        self.left()
        self.html_template = ["<div%s>", "", "</div>"]



class Presentation(Thing):
    '''
    Class for the presentatoin. This is the outermost container for
    all of the presentation's objects. Its childredn should all be
    L{Page} instances.

    The html code is compiled by putting together the contents of a
    header html file, the copmiled html code of the childrem and a
    footer html file. The header and footer are string templates.
    header takes one parameter: the inline CSS style tag.
    footer takes 3 template parameters: width(int), height(int), theme(str)
    '''
    def __init__(self, **kwargs):
        '''
        @keyword theme_reveal: the reveal theme to use.
        @keyword theme: a L{Theme} instance to use as custom theme.
        @keyword width: the reveal width of the presentation.
        @keyword height: the reveal height of the presentation.
        @keyword scale: the font size scale for the presentation.
        @keyword data_dir: main directory for media files.
        @todo: properly implement the scale parameter.
        '''
        Thing.__init__(self)
        self.theme_reveal = kwargs.get('theme_reveal', 'default')
        self.theme = kwargs.get('theme')
        self.width = kwargs.get('width', '1280')
        self.height = kwargs.get('height', '1024')
        self.scale = kwargs.get('scale', 1)
        self.slideNumber = kwargs.get('slideNumber', 'true')
        self.autoSlide = kwargs.get('autoSlide', 'false')
        self.progress = kwargs.get('autoSlide', 'true')
        self.controls = kwargs.get('autoSlide', 'true')
        self.loop = kwargs.get('loop', 'false')
        self.embedded = kwargs.get('embedded', 'false')
        self.center = kwargs.get('center', 'true')
        self.history = kwargs.get('history', 'true')
        self.margin = kwargs.get('margin', '0.1')
        self.transition = kwargs.get('transition', 'linear')
        self.data_dir = kwargs.get('data_dir')

        # MathJax
        self.mathjax_url_remote = 'http://cdn.mathjax.org/mathjax/latest/MathJax.js'
        self.mathjax_url_local = './lib/MathJax/MathJax.js'
        self.config_mathjax()

        self.css({"font-size":str(int(self.scale * 100)) + "%"})

        with open(filename_header) as f:
            self.template_header = Template(f.read())
            self.inline_style = self.theme.export_style() if self.theme else ""
            self.header = self.template_header.substitute(inlinestyle=self.inline_style,
                                                          mathjax_src=self.mathjax_src)
        with open(filename_footer) as f:
            self.template_footer = Template(f.read())
            self.footer = self.template_footer.substitute(width=self.width,
                                                          height=self.height,
                                                          progress=self.progress,
                                                          controls=self.controls,
                                                          loop=self.loop,
                                                          embedded=self.embedded,
                                                          autoSlide=self.autoSlide,
                                                          slideNumber=self.slideNumber,
                                                          history=self.history,
                                                          center=self.center,
                                                          themeReveal=self.theme_reveal,
                                                          margin=self.margin,
                                                          transition=self.transition

                                                                          )
        self.html_template = ['<body%s>\n<div class="reveal">\n <div class="slides">',
                              "",
                              "</div>\n</div>\n</div>" + self.footer]
    def config_mathjax(self, **kwargs):
        '''
        Set the MathJax library url depending on whether
        local or remote versions should be used.
        '''
        self.mathjax = kwargs.get('mathjax', 'local')
        if self.mathjax == 'local':
            self.mathjax_src = self.mathjax_url_local
        else:
            self.mathjax_src = self.mathjax_url_remote


    def dig(self):
        s = []
        for c in self.children:
            s += ["    %s" % x for x in c.dig()]
        result = [self.header] + [self.html_template[0] % self.getHTMLOptions()] + s + [self.html_template[2]]
        return result


    def export(self, filename):
        '''
        Compile the html code for the presentation
        and export it to file.
        @param filename: the output filename.
        '''
        with open (filename, 'w') as f:
            for line in  self.dig():
                f.write(line + "\n")

    def addPage(self, page=None):
        '''
        Add a given page to presentation, or create
        a new one.
        @return: the page object.
        '''
        if not page:
            page = Page()
        self.add(page)
        return page

    def page(self, header="", **kwargs):
        '''
        Create and add a new child L{Page} with
        the given header text.
        @param header: the header text for the page.
        @return: the newly created page.
        '''
        p = Page(header, **kwargs)
        self.add(p)
        return p

    def pagesection(self, text=''):
        '''
        Create and add a new child L{PageSection} with
        the given header text.
        @param text: the header text for the page.
        @return: the newly created page.
        '''
        p = PageSection(text)
        self.add(p)
        return p

    def frontpage(self):
        '''
        Create and add a new child L{FrontPage}.
        @return: the newly created page.
        '''
        p = FrontPage()
        self.add(p)
        return p

    def endpage(self, **kwargs):
        '''
        Create and add a new child L{EndPage}.
        @return: the newly created page.
        '''
        p = EndPage(**kwargs)
        self.add(p)
        return p



class Vspace(Thing):
    '''
    Class for vertical space.
    '''
    def __init__(self, h="1em", **kwargs):
        '''
        @param h: CSS height of the vertical space.
        '''
        Thing.__init__(self, **kwargs)
        self.height = h
        self.css({'height':self.height, "clear":'both'})
        self.html_template = ["<div%s>", "", "</div>"]



class FrontPage(Page):
    '''
    Class for the presentation's frontpage.
    @ivar authors: list of author objects.
    '''
    def __init__(self, **kwargs):
        Page.__init__(self, **kwargs)
        self.authors = []
        self.is_built = False

    def build(self):
        '''
        Link the institutions to the authors and
        create L{Institution} objects.
        '''
        if not self.is_built:
            self.add(Vspace('1em'))
            dict_inst_authors = {}
            dict_insts = {}
            dict_inst_index = {}
            counter_inst = 1
            for author in self.authors:
                for inst in author.institutions:
                    try:
                        dict_inst_authors[inst.name].append(author)
                        inst.index = dict_inst_index[inst.name]
                    except:
                        dict_inst_authors[inst.name] = [author]
                        inst.index = counter_inst
                        dict_inst_index[inst.name] = counter_inst
                        counter_inst += 1
                        print "new inst:", inst.name
                        dict_insts[inst.name] = inst

            for inst_name, inst in sorted(dict_insts.items(), key=lambda x:x[1].index):
                self.add(inst)

            self.is_built = True

    def title(self, title=""):
        '''
        Set the title of the frontpage.
        @param title: the title of the frontpage.
        '''
        self.title = title
        h = self.addH2(title).css({"margin-bottom":"2em", "margin-top":"1em"}).cl('title')
        return h
    def author(self, name):
        '''
        Add an author to the frontpage.
        @param name: name of the author.
        '''
        author = Author(name).cl('author')
        self.add(author)
        self.authors.append(author)
        return author
    def dig(self):
        self.build()
        return Page.dig(self)



class EndPage(Page):
    '''
    Class for the last page: Thank you, contact info, etc.
    @todo: methods need more careful implementation.
    '''
    def __init__(self, **kwargs):
        '''
        Implement to customize the contents.
        '''
        Page.__init__(self, **kwargs)
        self.url_qr = kwargs.get('url_qr')
        self.email = kwargs.get('email', False)

        self.authors = []

        self.h2('Thank You!').cl('textshadow-large')
        self.author('Navid Dianati')
        if self.email:
            self.h4('navid.dianati@gmail.com').cl('email')
        if self.url_qr:
            self.qr(self.url_qr)
    def author(self, name):
        author = Author(name).cl('author')
        self.add(author)
        self.authors.append(author)
        return author
    def qr(self, url):
        image = self.im(url).w('30%')
        return image





class Author(H4):
    '''
    Class for an author for the presentation.
    @ivar institutions: list of associated institutions.
    '''
    def __init__(self, name='', **kwargs):
        '''
        @param name: name of the author.
        '''
        self.name = name
        H4.__init__(self, name, **kwargs)
        self.institutions = []

    def institution(self, name):
        '''
        Create and add a new Institution object.
        @param name: name of the institution.
        @return the newly created L{Institution} object.
        '''
        inst = Institution(name)
        self.institutions.append(inst)
        return inst
    def dig(self):
        s = ''
        if self.institutions:
            s = "<sup>%s</sup>" % ','.join([str(inst.index) for inst in sorted(self.institutions)])
        self.html += s
        return H4.dig(self)

class Institution(H4):
    '''
    Class for an institution for the presentation.
    '''
    def __init__(self, name='', **kwargs):
        '''
        @param name: name of the institution.
        '''
        self.name = name
        H4.__init__(self, name, **kwargs)
        self.index = None
    def dig(self):
        print self.index, self.name
        if self.index:
            self.html = ("<sup>%d</sup>" % self.index) + self.html
        return H4.dig(self)









if __name__ == "__main__":
    test()


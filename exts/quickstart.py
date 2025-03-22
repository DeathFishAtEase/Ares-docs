def setup(app):
    app.add_node(quickstart,
                 html=(visit_quickstart_node, depart_quickstart_node),
                 latex=(visit_quickstart_node, depart_quickstart_node),
                text=(visit_quickstart_node, depart_quickstart_node))

    app.add_directive('quickstart', QuickstartDirective)

from docutils import nodes

class quickstart(nodes.Admonition, nodes.Element):
    pass

def visit_quickstart_node(self, node):
    self.visit_admonition(node)

def depart_quickstart_node(self, node):
    self.depart_admonition(node)


from docutils.parsers.rst import Directive

class QuickstartDirective(Directive):

    # this enables content in the directive
    has_content = True

    def run(self):
        env = self.state.document.settings.env

        targetid = f"quickstart-{env.new_serialno('quickstart')}"
        targetnode = nodes.target('', '', ids=[targetid])

        # 创建自定义的quickstart节点
        ad_node = quickstart()
        ad_node['classes'] = self.options.get('class', []) + ['admonition']

        # 添加标题
        title_text = 'Quickstart'
        textnodes, messages = self.state.inline_text(title_text, self.lineno)
        title = nodes.title(title_text, '', *textnodes)
        ad_node += title

        # 解析指令内容
        content_node = nodes.container()
        self.state.nested_parse(self.content, self.content_offset, content_node)
        ad_node += content_node

        return [targetnode, ad_node] + messages

import ast

# 示例Python代码
source_code = 'x = 1 + 2'

# 使用ast.parse()生成AST
tree = ast.parse(source_code)

# 打印AST结构
print(ast.dump(tree, indent=4))

def generate_pascal_triangle(n):
    row = [1]
    for _ in range(n):
        yield row
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]

# 测试生成器
n = int(input("请输入要生成的杨辉三角的行数："))
triangle_generator = generate_pascal_triangle(n)
for row in triangle_generator:
    print(row)

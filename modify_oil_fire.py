# -*- coding: utf-8 -*-
import re

# 读取文件
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 旧代码模式
old_oil_fire = '''            if (preset === 'oil-fire') {
                for (let x = 100; x < 500; x += 15) {
                    for (let y = 300; y < 400; y += 15) {
                        if (Math.random() < 0.7) {
                            grid[y][x] = TYPE_OIL;
                        }
                    }
                }

                for (let x = 150; x < 450; x += 20) {
                    const y = 280 + Math.floor(Math.random() * 20);
                    if (isValid(x, y)) {
                        grid[y][x] = TYPE_FIRE;
                    }
                }
            }'''

# 新代码：油水效果
new_oil_fire = '''            if (preset === 'oil-fire') {
                // 底层石油：x=150-650, y=380-480, 密度0.8
                for (let x = 150; x < 650; x += 12) {
                    for (let y = 380; y < 480; y += 12) {
                        if (Math.random() < 0.8) {
                            grid[y][x] = TYPE_OIL;
                        }
                    }
                }

                // 上方水流：x=100-700, y=280-380, 密度0.7
                for (let x = 100; x < 700; x += 10) {
                    for (let y = 280; y < 380; y += 10) {
                        if (Math.random() < 0.7) {
                            grid[y][x] = TYPE_WATER;
                        }
                    }
                }
            }'''

# 替换
new_content = content.replace(old_oil_fire, new_oil_fire)

# 写入文件
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("修改完成！")

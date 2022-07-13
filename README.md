# clipboard 剪切板

## 项目说明

该项目用于记录剪切板中的内容。使用密钥加密 clipboard.priv.txt 中的内容，获取后再提取明文文本

## 项目思路

### 目录结构

```json
{
    'clipboard': '二进制文件 密文文件', 
    'clipboard.priv.txt': '明文文本 在 .gitignore 中忽略', 
    '.gitignore': '暂定忽略 venv, *.priv*', 
    'stamp_xxxxxx.priv': '空文件 文件名为加密密钥', 
    'venv': 'python 虚拟环境 ignore', 
    'CipherCylinder.py': '密码筒 py 文件 用于加密解密', 
}
```

### 实施流程

1. 以读取 clipboard.priv.txt 文件

2. 获取随机6位密钥

3. 使用密钥加密文件，以二进制文件保存
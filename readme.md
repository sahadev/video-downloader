# 视频下载工具

一个功能强大的视频下载脚本，支持多种视频平台，包括普通视频链接、YouTube 和 Bilibili。

## 功能特性

- ✅ 支持普通视频链接（直接 MP4 等格式）
- ✅ 支持 YouTube 视频下载
- ✅ 支持 Bilibili 视频下载（包括标准链接和短链接）
- ✅ 自动选择最佳可用格式
- ✅ 自动合并视频和音频流
- ✅ 支持指定输出目录
- ✅ 支持指定视频质量
- ✅ 显示下载进度和视频信息

## 环境要求

- Python 3.6+
- ffmpeg（用于合并视频和音频流）

## 安装步骤

### 1. 克隆或下载项目

```bash
cd video-download
```

### 2. 创建虚拟环境（推荐）

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate  # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 安装 ffmpeg（如果未安装）

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**
下载并安装 [ffmpeg](https://ffmpeg.org/download.html)，或使用包管理器如 Chocolatey:
```bash
choco install ffmpeg
```

## 使用方法

### 基本用法

```bash
python download_video.py <视频链接>
```

**注意**: 默认情况下，视频会下载到项目目录下的 `downloads/` 文件夹中。该文件夹已添加到 `.gitignore`，不会被提交到 Git 仓库。

### 下载普通视频

```bash
python download_video.py https://www.getsnippets.ai/why-keeping-prompts/ikea-veo.mp4
```

### 下载 YouTube 视频

```bash
python download_video.py https://www.youtube.com/watch?v=VIDEO_ID
```

### 下载 Bilibili 视频

**标准链接:**
```bash
python download_video.py https://www.bilibili.com/video/BVxxxxx
```

**短链接:**
```bash
python download_video.py https://b23.tv/xxxxx
```

### 指定输出目录

```bash
python download_video.py <视频链接> -o ./videos
```

如果不指定输出目录，视频会默认下载到项目目录下的 `downloads/` 文件夹。

### 指定视频质量

```bash
python download_video.py <视频链接> -q 720p
```

质量选项示例：
- `best` - 最佳质量（默认）
- `worst` - 最低质量
- `720p` - 720p 分辨率
- `1080p` - 1080p 分辨率

### 完整示例

```bash
# 下载 YouTube 视频到指定目录
python download_video.py https://www.youtube.com/watch?v=VIDEO_ID -o ./downloads

# 下载 Bilibili 视频，指定 720p 质量
python download_video.py https://www.bilibili.com/video/BVxxxxx -q 720p -o ./videos
```

## 命令行参数

```
positional arguments:
  url                   视频链接 URL

optional arguments:
  -h, --help            显示帮助信息
  -o, --output DIR      指定输出目录（默认为项目目录下的 downloads 文件夹）
  -q, --quality QUALITY 指定视频质量（如: best, worst, 720p, 1080p 等）
```

## 注意事项

1. **Bilibili 视频**: 脚本会自动选择可用的最佳格式，某些需要会员的高码率格式可能无法下载。如需下载会员专享内容，请参考 [yt-dlp 文档](https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp) 使用 cookies 进行身份验证。

2. **YouTube 视频**: 某些视频可能需要 JavaScript 运行时才能获取完整信息，但脚本仍可正常下载。

3. **文件命名**: 下载的文件会使用视频标题作为文件名，特殊字符会被自动处理。

4. **临时文件**: 下载过程中会创建临时文件，下载完成后会自动清理。

## 故障排除

### 问题：提示需要 ffmpeg

**解决方案**: 安装 ffmpeg（见上方安装步骤）

### 问题：Bilibili 视频下载失败，提示格式不可用

**解决方案**: 
- 脚本会自动回退到可用格式
- 如果仍然失败，可以尝试指定较低的质量：`-q 720p` 或 `-q worst`

### 问题：YouTube 视频下载失败

**解决方案**:
- 检查网络连接
- 确认视频链接有效
- 某些地区可能需要代理

## 技术栈

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - 强大的视频下载工具
- [ffmpeg](https://ffmpeg.org/) - 视频处理工具

## 许可证

本项目仅供学习和个人使用，请遵守各视频平台的使用条款。

#!/usr/bin/env python3
"""
视频下载脚本
支持普通视频链接、YouTube 链接和 Bilibili 视频
"""

import os
import sys
import argparse
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    print("错误: 未安装 yt-dlp。请运行: pip install yt-dlp")
    sys.exit(1)


def download_video(url, output_dir=None, quality=None):
    """
    下载视频
    
    Args:
        url: 视频链接
        output_dir: 输出目录（默认为项目目录下的 downloads 文件夹）
        quality: 视频质量（可选，如 'best', 'worst', '720p' 等）
    """
    if output_dir is None:
        # 默认输出目录为项目目录下的 downloads 文件夹
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, 'downloads')
    else:
        output_dir = os.path.abspath(output_dir)
    
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 配置 yt-dlp 选项
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'format': quality or 'best',
    }
    
    # 如果是 YouTube 链接，可以添加更多选项
    if 'youtube.com' in url or 'youtu.be' in url:
        ydl_opts.update({
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        })
    
    # Bilibili 视频支持（yt-dlp 原生支持）
    # 支持 bilibili.com 和 b23.tv 短链接
    # 使用格式选择器自动回退到可用格式，避免选择需要会员的格式
    if 'bilibili.com' in url or 'b23.tv' in url:
        if quality:
            # 如果用户指定了质量，使用指定的质量
            ydl_opts['format'] = quality
        else:
            # 否则使用自动回退格式选择器，优先选择最佳可用格式
            ydl_opts['format'] = 'bestvideo+bestaudio/best'
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"开始下载: {url}")
            print(f"输出目录: {output_dir}")
            
            # 获取视频信息
            info = ydl.extract_info(url, download=False)
            print(f"视频标题: {info.get('title', '未知')}")
            print(f"视频时长: {info.get('duration', 0)} 秒")
            print(f"文件大小: {info.get('filesize', 0) / (1024*1024):.2f} MB" if info.get('filesize') else "未知")
            
            # 下载视频
            ydl.download([url])
            print("下载完成！")
            
    except Exception as e:
        print(f"下载失败: {str(e)}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='视频下载工具 - 支持普通视频链接、YouTube 和 Bilibili',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 下载普通视频
  python download_video.py https://www.getsnippets.ai/why-keeping-prompts/ikea-veo.mp4
  
  # 下载 YouTube 视频
  python download_video.py https://www.youtube.com/watch?v=VIDEO_ID
  
  # 下载 Bilibili 视频
  python download_video.py https://www.bilibili.com/video/BVxxxxx
  python download_video.py https://b23.tv/xxxxx
  
  # 指定输出目录
  python download_video.py URL -o ./videos
  
  # 指定视频质量
  python download_video.py URL -q 720p
        """
    )
    
    parser.add_argument('url', help='视频链接 URL')
    parser.add_argument('-o', '--output', dest='output_dir', 
                       help='输出目录（默认为项目目录下的 downloads 文件夹）')
    parser.add_argument('-q', '--quality', dest='quality',
                       help='视频质量（如: best, worst, 720p, 1080p 等）')
    
    args = parser.parse_args()
    
    download_video(args.url, args.output_dir, args.quality)


if __name__ == '__main__':
    main()


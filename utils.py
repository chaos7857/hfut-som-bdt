import requests
import os

def download_image(url, save_dir, phpsessid):
    try:
        response = requests.get(
            url,
            cookies={"PHPSESSID": phpsessid},
            stream=True,
            timeout=10
        )
        response.raise_for_status()
        
        # 生成文件名
        filename = os.path.basename(url.split('?')[0])
        save_path = os.path.join(save_dir, filename)
        
        # 保存图片
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        return filename
    
    except Exception as e:
        print(f"图片下载失败: {url} - {str(e)}")
        return None
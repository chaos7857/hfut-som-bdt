import requests

def get_stu_task(task_id, cid, phpsessid, base_url="http://your-domain.com"):
    url = f"{base_url}/student/studentCourse/getTaskDetail"
    payload = {
        "courseId": cid,
        "taskId": task_id
    }
    cookies = {
        "PHPSESSID": phpsessid  # 添加会话Cookie
    }

    try:
        # 发送携带Cookie的POST请求
        response = requests.post(
            url,
            data=payload,
            cookies=cookies,  # 注入Cookie
            timeout=10
        )
        response.raise_for_status()
        
        redata = response.json()
        
        if redata.get("status") == 1:
            data = redata.get("datas", {})
            topo_id = data.get("topoId")
            stu_task_state = data.get("stuTaskState")
            
            print(f"[DEBUG] 拓扑ID: {topo_id}")
            # 其他业务逻辑...
            return redata
        else:
            print(f"请求失败，状态码: {redata.get('status')}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"请求异常: {str(e)}")
        return None
    except ValueError as e:
        print(f"JSON解析失败: {str(e)}")
        return None

# 使用示例
if __name__ == "__main__":
    # 需要替换为实际参数
    task_id = "5467"
    cid = "284"
    session_id = "2qa0ug365a4pmp8qcmmk96d786"  # 替换实际PHPSESSID
    base_url = "http://10.200.64.39"
    
    result = get_stu_task(task_id, cid, session_id, base_url)
    if result:
        print("请求成功，返回数据:", result)
import json
import random
from datetime import datetime

data_list = []
roles = ["admin", "user", "manager", "guest"]

for i in range(1, 1001):
    record = {
        "id": i,
        "name": f"User_{i}",
        "email": f"user_{i}@example.com",
        "age": random.randint(18, 60),
        "role": random.choice(roles),
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "is_active": random.choice([True, False])
    }
    data_list.append(record)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data_list, f, indent=4, ensure_ascii=False)

print("Đã tạo thành công file 'data.json' với 1000 bản ghi!")
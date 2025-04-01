import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc file CSV
df = pd.read_csv("salaries.csv")

# Hiển thị thông tin tổng quan
print('Hiển thị 5 dòng')
print(df.head())

print('Hiển thị thông tin chi tiết về DataFrame')
print(df.info())

print('Hiển thị các thống kê mô tả')
print(df.describe())

# Mức lương trung bình theo quốc gia

print(df.groupby("company_location")["salary"].mean())


# Mức lương trung bình theo số năm kinh nghiệm
#print(df.groupby("employee_residence")["salary"].mean())


#plt.figure(figsize=(10, 6))
#sns.boxplot(x="company_location", y="salary", data=df)
#plt.xticks(rotation=90)
#plt.title("Mức lương Data Engineer theo quốc gia")
#plt.show()

# Tính mức lương trung bình theo loại hợp đồng
average_salaries = df.groupby('employment_type')['salary_in_usd'].mean().reset_index()

# Sắp xếp theo mức lương giảm dần
average_salaries = average_salaries.sort_values(by='salary_in_usd', ascending=False)

# Vẽ biểu đồ cột
plt.figure(figsize=(10, 6))
colors = plt.cm.Paired.colors[:len(average_salaries)]  # Chọn màu tự động theo số loại employment_type
plt.bar(average_salaries['employment_type'], average_salaries['salary_in_usd'], color=colors)

# Cải thiện hiển thị
plt.xlabel('Loại Hợp Đồng', fontsize=12)
plt.ylabel('Mức lương trung bình (USD)', fontsize=12)
plt.title('Mức lương trung bình theo loại hợp đồng (2024)', fontsize=14, fontweight="bold")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Hiển thị giá trị trên cột
for i, v in enumerate(average_salaries['salary_in_usd']):
    plt.text(i, v + 2000, f"${int(v):,}", ha='center', fontsize=10, fontweight='bold')

plt.show()

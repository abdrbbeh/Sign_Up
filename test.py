

import bcrypt

password = "mypassword".encode("utf-8")  # تحويل كلمة المرور إلى بايتات

# # إنشاء ملح عشوائي
salt = bcrypt.gensalt()

# تشفير كلمة المرور باستخدام الملح
# hashed_password = bcrypt.hashpw(password, salt)
# print(hashed_password)
# يمكنك حفظ "hashed_password" في قاعدة البيانات

# ############################################################372749



password2 = "Hamdo.1972".encode("utf-8")  # تحويل كلمة المرور إلى بايتات
stored_password = b'$2b$12$9gNkrtakD09/ARuDssM7Zu/QIZMl/p8XApIRz6Z4jDJ7s0U6t3jdy'  # احصل على كلمة المرور المشفرة من قاعدة البيانات

# التحقق من صحة كلمة المرور المقدمة
if bcrypt.checkpw(password2, stored_password):
    print("تم تسجيل الدخول بنجاح!")
else:
    print("كلمة المرور غير صحيحة!")
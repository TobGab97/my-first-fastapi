from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Stocks(models.Model):

    id = fields.IntField(pk=True)
    serial_number = fields.TextField(max_length=20, null=True)
    quantity = fields.IntField(max_length=5, null=True)
    row = fields.CharField(max_length=1, null=True)
    column = fields.IntField(max_length=2, null=True)
    added_at = fields.DatetimeField(auto_now=True)

Stock_Pydantic = pydantic_model_creator(Stocks, name="Stock")
StockIn_Pydantic = pydantic_model_creator(Stocks, name="StockIn", exclude_readonly=True)

#     def full_name(self) -> str:
#         """
#         Returns the best name
#         """
#         if self.name or self.family_name:
#             return f"{self.name or ''} {self.family_name or ''}".strip()
#         return self.username

#     class PydanticMeta:
#         computed = ["full_name"]
#         exclude = ["password_hash"]


# User_Pydantic = pydantic_model_creator(Users, name="User")
# UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)

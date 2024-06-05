from models import Order, User, Product
from schemas import OrderModel
from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from database import session, ENGINE

session = session(bind=ENGINE)


order_router = APIRouter(prefix="/orders")

@order_router.get('/')
async def orders():
    orders = session.query(Order).all()
    context = [
        {
            "id": order.id,
            "user_id": {
                "id": order.user.id,
                "first_name": order.user.first_name,
                "last_name": order.user.last_name,
                "username": order.user.username,
                "email": order.user.email,
                "is_staff": order.user.is_staff,
                "is_active": order.user.is_active,

            },
            "product_id": {
                "id": order.product.id,
                "name": order.product.name,
                "category": {
                    "id": order.product.categoryid,
                    "name": order.product.category.name
                }
            },
            "status": order.order_status
        }
        for order in orders
    ]
    return jsonable_encoder(context)

# @order_router.post("/create")


@order_router.post('/create')
async def create(order: OrderModel):
    check_order = session.query(Order).filter(Order.id == order.id).first()
    check_user_id = session.query(User).filter(User.id == order.user_id).first()
    check_product_id = session.query(Product).filter(Product.id == order.product_id).first()

    if check_order:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already exis")

    elif check_user_id and check_product_id:
        new_order = Order(
            id=order.id,
            user_id=order.user_id,
            product_id=order.product_id,
            order_status=order.order_status
        )
        session.add(new_order)
        session.commit()
        data = {
            "code": 201,
            "msg": "success"
        }
        return jsonable_encoder(data)

    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user_id or product_id allr exis")




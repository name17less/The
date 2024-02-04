from aiogram.types import LabeledPrice

from tgbot.misc.item import Item

Tesla_CyberSex = Item(
    title="Тесла КиберТрах",
    description="я гей",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="КиберТрах",
            amount=10000
        )
    ],
    start_parameter="create_invoice_tesla_cybersex",
    photo_url="https://s1.cdn.autoevolution.com/images/news/tesla-cybertruck-memes-aside-what-the-hell-is-wrong-with-tesla-139348_1.jpg",
    photo_size=600
)

Sanya = Item(
    title="Санечка Фомин",
    description="он гей",
    currency="RUB",
    prices=[
        LabeledPrice(
            label="санечка собственной персоной",
            amount=1_20
        ),
        LabeledPrice(
            label="скидка (заберите пожалуйста)",
            amount=-10_00
        ),
        LabeledPrice(
            label="НДС",
            amount=130_00
        )
    ],
    start_parameter="create_invoice_sanya",
    photo_url="https://kpravda.ru/wp-content/uploads/2023/10/fomin-533x533.png",
    photo_size=600
)
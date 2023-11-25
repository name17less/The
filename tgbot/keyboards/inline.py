from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Keyboard = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=
                                [
                                    [
                                        InlineKeyboardButton(
                                            text="Шишки",
                                            callback_data="sheesh"
                                        ),
                                        InlineKeyboardButton(
                                            text="Пышки",
                                            callback_data="peesh"
                                        )
                                    ],
                                    [
                                        InlineKeyboardButton(
                                            text="Назад",
                                            callback_data="cancel"
                                        )
                                    ]
                                ]
                                )

from typing import Final

GREETING_TEXT: Final[str] = """
Доброго времени суток Руслан!
Это главное меню, тут вы можете управлять перенаправлениями, удалять, изменять и добавлять их.
"""

SHOW_REDIRECT_TEMPLATE: Final[str] = """
- Перенаправление из {from_chat_name} - ({from_chat_id}) в {to_chat_name} - ({to_chat_id}) 

"""

BACK_BUTTON_TEXT: Final[str] = "🔙 Назад"

CREATE_NEW_REDIRECT_TEXT: Final[str] = """
Для создания нового перенаправления, пожалуйста, отправьте ID телеграм канала 
с которого должно осуществляться копирование постов.
"""

EDIT_REDIRECT_TEXT: Final[str] = """
Для того чтобы изменить перенаправление выберите его в списке ниже
"""

ASK_FOR_COPY_FROM_CHAT_ID_TEXT: Final[str] = """
Пожалуйста введите ID канала из которого должно осуществляться копирование
"""

ASK_FOR_COPY_TO_CHAT_ID_TEXT: Final[str] = """
Пожалуйста введите ID канала куда должно осуществляться копирование
"""

ASK_TO_TRY_AGAIN: Final[str] = """
Что-то пошло не так. Пожалуйста, проверьте правильность введенного ID и повторите попытку. 
В случае, если ошибка продолжает возникать, пожалуйста, сообщите об этом разработчику
"""

ASK_CONFIRMATION_FOR_DELETING_ALL: Final[str] = """
Вы уверены что хотите удалить все перенаправления ?
"""

ASK_CONFIRMATION_FOR_DELETING_ONE: Final[str] = """
Вы уверены что хотите удалить это перенаправление ?
"""

ASK_CONFIRMATION_FOR_ADDING_NEW_REDIRECT: Final[str] = """
Вы уверены что хотите создать это перенаправление ?
"""

EMPTY_REDIRECTS_LIST_CASE: Final[str] = """
Перенаправления пока отсутсвуют...
"""
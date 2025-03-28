from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# Dữ liệu về khái niệm toán học
MATH_CONCEPTS = {
    "đạo hàm": "Đạo hàm là khái niệm trong giải tích mô tả tốc độ thay đổi của một hàm số...",
    "tích phân": "Tích phân là phép toán ngược của đạo hàm, được sử dụng để tính diện tích dưới đường cong...",
}

# Dữ liệu về công thức toán học
MATH_FORMULAS = {
    "đạo hàm": "f'(x) = lim(h -> 0) [f(x+h) - f(x)] / h",
    "tích phân": "\int f(x)dx = F(x) + C",
}

class ActionProvideMathConcept(Action):
    def name(self):
        return "action_provide_math_concept"

    def run(self, dispatcher, tracker, domain):
        concept = tracker.get_slot("math_concept")

        # Kiểm tra nếu slot bị None
        if not concept:
            dispatcher.utter_message(text="Bạn có thể cung cấp rõ hơn khái niệm toán học bạn muốn tìm không?")
            return []

        response = MATH_CONCEPTS.get(concept.lower(), "Xin lỗi, tôi chưa có thông tin về khái niệm này.")
        dispatcher.utter_message(text=response)
        return []

class ActionProvideMathFormula(Action):
    def name(self):
        return "action_provide_math_formula"

    def run(self, dispatcher, tracker, domain):
        formula = tracker.get_slot("math_formula")

        # Kiểm tra nếu slot bị None
        if not formula:
            dispatcher.utter_message(text="Bạn có thể cung cấp rõ hơn công thức toán học bạn muốn tìm không?")
            return []

        response = MATH_FORMULAS.get(formula, "Xin lỗi, tôi chưa có công thức cho nội dung này.")
        dispatcher.utter_message(text=response)
        return []

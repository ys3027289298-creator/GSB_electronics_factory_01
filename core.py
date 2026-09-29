"""电子厂核心逻辑：元件、贴片机、回流焊和检测。"""

import json


def new_game():
    return {
        "orders": {},
        "machine_load": 0,
        "machine_capacity": 2,
        "components": 100,
        "yield_rate": 100,
        "order_id": 0,
    }


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["order_id"] += 1
    return state


def feed(self, order_id, amount):
    self["orders"][order_id] = amount
    self["machine_load"] += amount
    self["components"] -= amount
    return True


def check_temp(self, temp):
    if temp < 30:
        return "over"
    return "ok"


def cancel(self, order_id):
    return True


def produce(self, amount):
    return True


def static_event(self):
    self["yield_rate"] -= 5
    self["yield_rate"] -= 5
    return self["yield_rate"]


def place(self, amount):
    return True


def main():
    print("电子厂 - 命令: feed/temp/cancel/produce/static/place/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()

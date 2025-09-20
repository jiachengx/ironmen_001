def on_button_pressed_ab():
    pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# 第七章：第一次的失敗 - 錯誤程式碼
# 描述：忘了考慮「同時按下」的情境，使用兩個獨立的 if 判斷式
# 顯示右箭頭

def on_forever():
    # 如果按下按鈕 A
    if input.button_is_pressed(Button.A):
        basic.show_arrow(ArrowNames.WEST)
    # 顯示左箭頭
    # 如果按下按鈕 B
    if input.button_is_pressed(Button.B):
        basic.show_arrow(ArrowNames.EAST)
basic.forever(on_forever)

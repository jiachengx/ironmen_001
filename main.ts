input.onButtonPressed(Button.AB, function () {
	
})
// 第七章：第一次的失敗 - 錯誤程式碼
// 描述：忘了考慮「同時按下」的情境，使用兩個獨立的 if 判斷式
// 顯示右箭頭
basic.forever(function () {
    // 如果按下按鈕 A
    if (input.buttonIsPressed(Button.A)) {
        basic.showArrow(ArrowNames.West)
    }
    // 顯示左箭頭
    // 如果按下按鈕 B
    if (input.buttonIsPressed(Button.B)) {
        basic.showArrow(ArrowNames.East)
    }
})

-- 🍂 Abyss Calculation - Elm Edition
-- The Most Frontend-Functional 1+1 Calculator!

module Abyss exposing (main)

import Browser
import Html exposing (Html, text, div, h1, p)
import Task
import Process

type Msg = Calculate | Result Int

quantumEntangle : Int -> Cmd Msg
quantumEntangle value =
    Task.perform (always (Result value)) (Process.sleep 800)

update : Msg -> Int -> (Int, Cmd Msg)
update msg model =
    case msg of
        Calculate ->
            (0, Cmd.batch [ quantumEntangle 1, quantumEntangle 1 ])
        
        Result value ->
            let newModel = model + value
            in
            if newModel == 2 then
                (newModel, Cmd.none)
            else
                (newModel, Cmd.none)

view : Int -> Html Msg
view model =
    div []
        [ h1 [] [ text "🌌 ELM ABYSS CALCULATION" ]
        , p [] [ text "   NO RUNTIME ERRORS GUARANTEED" ]
        , p [] [ text ("🎉 Functional result: " ++ String.fromInt model) ]
        ]

main : Program () Int Msg
main =
    Browser.element
        { init = \_ -> (0, Cmd.none)
        , update = update
        , view = view
        , subscriptions = \_ -> Sub.none
        }

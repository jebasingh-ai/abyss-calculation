/* 🎨 Abyss Calculation - ReasonML Edition
   The Most OCaml-But-JavaScripty 1+1 Calculator! */

let quantumEntangle = value => {
  Js.log("   🔮 Entangling quantum state...");
  Js.Promise.make((~resolve, ~reject as _) => {
    ignore(Js.Global.setTimeout(() => resolve(. value), 800));
  });
};

let wavefunctionCollapse = value => {
  Js.log("   ⚡ Collapsing wavefunction...");
  Js.Promise.make((~resolve, ~reject as _) => {
    ignore(Js.Global.setTimeout(() => resolve(. value), 600));
  });
};

let main = () => {
  Js.log("🌌 REASONML ABYSS CALCULATION");
  Js.log("   BUCKLESCRIPT POWER ACTIVATED");
  Js.log("");

  open Js.Promise;

  quantumEntangle(1)
  |> then_(quantum1 =>
       quantumEntangle(1)
       |> then_(quantum2 =>
            wavefunctionCollapse(quantum1)
            |> then_(collapsed1 =>
                 wavefunctionCollapse(quantum2)
                 |> then_(collapsed2 => {
                      let result = collapsed1 + collapsed2;
                      Js.log2("🎉 Reasonable result: ", result);
                      Js.log("   Type-safe JavaScript! 🎯");
                      resolve(result);
                    })
               )
          )
     )
  |> ignore;
};

main();

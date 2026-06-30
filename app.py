<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Algorithmic Password Evaluator</title>
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/@stlite/browser@1.7.0/build/style.css"
    />
  </head>
  <body>
    <div id="root"></div>
    <script type="module">
      import { mount } from "https://cdn.jsdelivr.net/npm/@stlite/browser@1.7.0/build/stlite.js";

      fetch("app.py")
        .then((response) => response.text())
        .then((code) => {
          mount(
            {
              requirements: ["pandas", "numpy", "plotly", "pyarrow"],
              entrypoint: "app.py",
              files: {
                "app.py": code,
              },
            },
            document.getElementById("root")
          );
        });
    </script>
  </body>
</html>

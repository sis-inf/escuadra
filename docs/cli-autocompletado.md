git checkout -b dev upstream/dev
git checkout dev
git checkout docs/cli-autocompletado
git reset --hard dev
nano docs/cli-autocompletado.md
git add docs/cli-autocompletado.md
git commit -m "docs: crear docs/cli-autocompletado.md — documentar el autocompletado de shell para el CLI

- Se documenta cómo activar autocompletado en bash/zsh/fish
- Se incluyen instrucciones paso a paso
- Se agrega ejemplo de uso y solución de problemas

Closes #789"
git push origin docs/cli-autocompletado --force

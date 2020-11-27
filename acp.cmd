set /p msg="Comentario del commit: "
git add -A && git commit -m "%msg%" && git push


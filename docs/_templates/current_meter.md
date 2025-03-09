```dataviewjs
let home=dv.page("/_obsidian/Homepage")
const {MyUtils}=await cJS()
dv.paragraph(MyUtils.current_meter(dv.current(),dv.page("_templates/current_meter"),home))
```

const SITE_TITLE = "狡兔百窟"
const SITE_DESCRIPTION = "兔子草的线上存档"
const LIGHT_THEME = "mylight"
const DARK_THEME = "mydark"
const EXTRA_TAGS: any[] = ["FIN", "TBC", "AI评论"]

import rehypeStringify from "rehype-stringify"
import remarkGfm from "remark-gfm"
import remarkParse from "remark-parse"
import remarkRehype from "remark-rehype"
import { unified } from "unified"

const processor = unified()
  .use(remarkParse)
  .use(remarkGfm)
  .use(remarkRehype, { allowDangerousHtml: true })
  .use(rehypeStringify)

const cateName = {
  dc: "DC",
  ai: "评论",
}

const date = (data: any) =>
  data.date ? data.date : data.auto_date || new Date()

export {
  SITE_TITLE,
  SITE_DESCRIPTION,
  LIGHT_THEME,
  DARK_THEME,
  EXTRA_TAGS,
  processor,
  cateName,
  date,
}

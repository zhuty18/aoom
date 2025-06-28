const SITE_TITLE = "狡兔百窟"
const SITE_DESCRIPTION = "兔子草的线上存档"
const LIGHT_THEME = "mylight"
const DARK_THEME = "mydark"
const EXTRA_TAGS: any[] = ["FIN", "TBC", "AI评论"]

import { unified } from "unified"
import remarkParse from "remark-parse"
import remarkGfm from "remark-gfm"
import remarkRehype from "remark-rehype"
import rehypeRaw from "rehype-raw"
import rehypeStringify from "rehype-stringify"

const processor = unified()
  .use(remarkParse)
  .use(remarkGfm)
  .use(remarkRehype, { allowDangerousHtml: true })
  .use(rehypeRaw)
  .use(rehypeStringify)

const cateName = {
  ai: "评论",
  blob: "片段",
  dc: "DC",
  dm: "数码宝贝",
  dmc: "鬼泣",
  dr: "龙族",
  ft: "童话系列",
  gtm: "银魂",
  m: "漫威",
  on: "原创",
  others: "其他",
  qz: "全职",
  swy: "食物语",
  translation: "翻译",
  x: "X战警",
  xj: "仙剑",
  ywj: "曳尾记",
  yys: "阴阳师",
}

const date = (data: any) =>
  data.date ? data.date : data.auto_date || new Date()

const SITE_ROOT = "/aoom"

const linkSite = (url: string) => SITE_ROOT + url

const linkStory = (id: string) => SITE_ROOT + `/docs/${id}`

export {
  SITE_TITLE,
  SITE_DESCRIPTION,
  LIGHT_THEME,
  DARK_THEME,
  EXTRA_TAGS,
  processor,
  cateName,
  date,
  linkSite,
  linkStory,
}

class MyUtils {
  work_of (pages, slice_at = null) {
    let tmp = pages
      .where((x) => x.word_count && x.file.folder.indexOf("trash") < 0)
      .sort((x) => x.word_count, "desc")
      .sort((x) => (x.date ? x.date : x.auto_date), "desc")
    if (slice_at) {
      return tmp
        .slice(0, slice_at)
        .sort((x) => (x.finished ? x.finished : false))
    }
    return tmp.sort((x) => (x.finished ? x.finished : false))
  }

  meter_at (value, global) {
    const colors = [
      //hsl(60, 90%, 60%)
      { h: 60, s: 90, l: 60, v: 0 },
      //hsl(330, 85%, 55%)
      { h: 330, s: 85, l: 55, v: global.percent_low },
      //hsl(220, 80%, 65%)
      { h: 220, s: 80, l: 65, v: global.percent_high },
      //hsl(160, 74.90%, 50.00%)
      { h: 160, s: 75, l: 50, v: global.percent_ideal },
      //hsl(120, 60%, 45%)
      { h: 120, s: 60, l: 45, v: 1 },
    ]
    let p = value
    let color = "hsl(0,100%,50%)"
    for (let i = 0; i < colors.length - 1; i++) {
      if (colors[i].v <= p && p <= colors[i + 1].v) {
        let start_color = colors[i]
        let end_color = colors[i + 1]
        let position = (p - start_color.v) / (end_color.v - start_color.v)

        let h_inter =
          Math.abs(end_color.h - start_color.h) > 180
            ? end_color.h - start_color.h - 360
            : end_color.h - start_color.h
        let h = start_color.h + position * h_inter
        h = h < 0 ? h + 360 : h > 360 ? h - 360 : h
        let s = start_color.s + position * (end_color.s - start_color.s)
        let l = start_color.l + position * (end_color.l - start_color.l)
        color = `hsl(${h},${s}%,${l}%)`
        break
      }
    }
    return `<meter class="tuzicao" value=${value} min=0 max=1 style="--progress-color: ${color};"></meter>`
  }

  percent_meter (value, global, line = 1) {
    if (line == 1) {
      return Math.round(value * 1000) / 10 + "%" + this.meter_at(value, global)
    } else {
      return (
        Math.round(value * 1000) / 10 + "%<br>" + this.meter_at(value, global)
      )
    }
  }

  count_by_size (size) {
    let size_fit = [
      { s: 0.32424175437273367, i: -36.62907210800612, min: 0, max: 18000 },
      { s: 0.32538376536796265, i: -77.70050272955389, min: 18000, max: 80000 },
      { s: 0.28972899603899527, i: 3823.615283001374, min: 80000, max: 140000 },
      { s: 0.3293464811684735, i: -421.2721915636414, min: 140000, max: -1 },
    ]
    for (let i = 0; i < size_fit.length; i++) {
      if (
        size >= size_fit[i].min &&
        (size < size_fit[i].max || size_fit[i].max == -1)
      ) {
        return Math.max(Math.round(size_fit[i].s * size + size_fit[i].i), 0)
      }
    }
  }

  count (page) {
    return this.count_by_size(page.file.size)
  }

  count_sum (pages) {
    return pages.map((x) => this.count(x)).sum()
  }

  count_text (value) {
    if (value < 20000) {
      return Math.round(value) + "字"
    } else {
      return Math.round(value / 100) / 100 + "万字"
    }
  }

  count_meter (page, global, line = 1, count_res = null) {
    if (count_res == null) {
      count_res = this.count(page)
    }
    let percent = 1
    if (!page.finished) {
      percent =
        count_res /
        Math.max(count_res / global.percent_ideal, global.count_ideal)
    }
    if (line == 1) {
      return (
        "🐰".repeat(parseInt(count_res / global.count_unit)) +
        this.meter_at(
          (count_res % global.count_unit) / global.count_unit,
          global
        ) +
        " " +
        this.count_text(count_res)
      )
    } else {
      return (
        this.count_text(count_res) + "<br>" + this.meter_at(percent, global)
      )
    }
  }

  current_meter (page, template, global, line = 1) {
    return this.count_meter(
      page,
      global,
      line,
      this.count_by_size(page.file.size - template.file.size)
    )
  }

  last_update (page) {
    return Math.floor(
      (Date.now() - Date.parse(page.date ? page.date : page.auto_date)) /
      1000 /
      60 /
      60 /
      24
    )
  }

  last_update_str (page, global) {
    let days = this.last_update(page)
    if (days == 0) {
      return "今天"
    } else if (days == 1) {
      return "昨天"
    } else if (days == 2) {
      return "前天"
    } else if (days <= global.day_awhile) {
      return days + "天前"
    } else {
      let date = new Date(page.date ? page.date : page.auto_date)
      return `${date.getFullYear()}年${date.getMonth() + 1
        }月${date.getDate()}日`
    }
  }

  pin_of (page, global) {
    return (
      "- [" +
      (this.last_update(page) <= Number(global.day_ideal) ? "f" : "n") +
      "] "
    )
  }

  short_text (page, global, tag_number = 2) {
    return (
      this.pin_of(page, global) +
      page.file.link +
      " " +
      page.file.tags.slice(0, tag_number).join(" ") +
      " " +
      this.count_meter(page, global)
    )
  }

  pages_raw_data (pages, global) {
    let all = this.work_of(pages)
    let tbc = all.where((page) => !page.finished)
    let fin = all.where((page) => page.finished)
    return {
      tbc: tbc.length,
      fin: fin.length,
      all: all.length,
      fin_percent: fin.length / all.length,
      tbc_count: this.count_sum(tbc),
      fin_count: this.count_sum(fin),
      all_count: this.count_sum(all),
      fin_count_avg: fin.map((page) => this.count(page)).avg(),
      fin_count_theory:
        this.count_sum(fin) +
        tbc
          .map((x) =>
            Math.max(global.count_ideal, this.count(x) / global.percent_ideal)
          )
          .sum(),
    }
  }

  pages_data (pages, name, global) {
    // "名称","坑数","完结率","坑字数","完结字数比","平均完结字数"
    let raw_data = this.pages_raw_data(pages, global)
    return [
      name,
      raw_data.tbc,
      this.percent_meter(raw_data.fin_percent, global, 2),
      this.count_text(raw_data.tbc_count),
      this.percent_meter(raw_data.fin_count / raw_data.all_count, global, 2),
      this.count_text(raw_data.fin != 0 ? raw_data.fin_count_avg : 0),
    ]
  }
}

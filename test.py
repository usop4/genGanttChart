import genGanttChart

gchart = GanttChart( (720, 320),(255,255,255) )
gchart.draw_calendar()
gchart.draw_campain("2019-10-15","2019-10-18","こんにちは")
gchart.draw_campain("2019-10-20","2019-10-23","こんにちは")
gchart.draw_campain("2019-10-24","2019-10-30","こんにちは")
gchart.draw_campain("2019-10-28","2019-10-30","こんにちは")
gchart.draw_campain("2019-10-29","2019-10-30","こんにちは")
gchart.show()
gchart.save("test.png")
    

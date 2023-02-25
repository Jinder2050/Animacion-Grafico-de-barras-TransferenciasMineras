from visualizer import Animation as am

# ===========================  DARK MODE ============================== #

def main():
    a = am.Darkanimation(filepath='assets\data\data.xlsx', duration=1, fps=60, bars_colors='assets\colors.json', anim_subtitle='2010 - 2022', anim_title='TRANSFERENCIA DE RECURSOS (Soles)')
    a.methods()



# ===========================  LIGHT MODE ============================== #

# def main():
#     a = am.Lightanimation(filepath='assets\data\data.xlsx', duration=1, fps=60, bars_colors='assets\colors.json', anim_subtitle='2010 - 2022', anim_title='TRANSFERENCIA DE RECURSOS', data_unit='S/.')
#     a.methods()

if __name__ == '__main__':
    main()
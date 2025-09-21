
    current_weight = float(input("请输入您当前的体重（kg）: "))
    
    # 月球体重转换率
    moon_ratio = 0.165
    
    print("\n年份\t地球体重(kg)\t月球体重(kg)")
    print("-" * 35)
    
    # 计算并输出未来10年的体重变化
    for year in range(1, 11):
        earth_weight = current_weight + 0.5 * year
        moon_weight = earth_weight * moon_ratio
        
        print(f"{year}\t{earth_weight:.2f}\t\t{moon_weight:.2f}")

if __name__ == "__main__":
    main()文件里编写代码

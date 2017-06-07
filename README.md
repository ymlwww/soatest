# soatest大作业——Tsinghua Guide
## 1.作业目标

​      实现一款能为清华游客提供电子景点浏览的app或者具有类似功能的网站。

​      需要实现的功能：

1. 规划校内景点的浏览路径
2. 校内景点的电子讲解
3. 校内景点的点赞和推荐
4. 类似导游对话似的人工智能服务



## 2. 设计思路

​       游客浏览清华的时间短则一个小时，长则半天到一天，一般不会有游客做长时间的停留，因为为了一些临时的旅游方便，游客下载一款app的概率很小，最多是扫描一个微信公众号，关注公众号获取相应信息，最简单的方式则是访问网页，但是我们了解到微信内置小应用的开发存在很大难度，所以最后决定做一个网站。

​        我们可以简单地将我们的网站功能分为两大块，一块是浏览路径的规划，一块是景点介绍和点赞推荐，至于人工智能对话则是锦上添花的任务，尽力而为就好。丁豪同学负责实现路径规划，喻明理同学负责景点介绍，汪佳欣同学负责数据收集整理和API搜索。路径规划中，我们可以选择一个或者多个景点以及行程的起点和终点，来规划出路径最短的游览路线，同时，学校的洗手间分布信息，以及各种学校活动的实时情况都可以同时获知。景点介绍则是选择了校内的十处景点作为测试，分别配备了景点的图片和文字音频介绍，游客可以在不同的景点下点赞和留言评论。

​        整体上我们的项目采用Python+Django的框架，也便于两个模块的合并，调用了Google和来必力的API（因为多说和一些国内通用的评论插件都被封了），基本实现了上述的所有功能，但是对于人工智能对话方便完全放弃，因为实现难度太大，也没有可以参考的已有例子，其次是图像识别的功能，我们发现，由于清华的景点特色很不明显，比如工字厅会被识别不出来具体的地点，只是显示是宫殿，而且是识别的精度受到拍摄角度，当天的天气等各种因素的影响，识别的准确度存在问题，再比如万人食堂，因为建的比较迟，所以很多地图上的实景上还没有相应的信息，最后能成功识别出来的只有二校门，大礼堂，二校门，主楼能识别出是清华大学，大礼堂能识别出比较精确的经纬度，但是名字还是清华大学，识别精度有待提高，所以没能实现这个功能，但是这种识别的可能性已经有科学家开始论证，详见https://scholar.google.com/citations?hl=zh-CN&user=d97bGd8AAAAJ&view_op=list_works和https://link.springer.com/chapter/10.1007/978-3-319-09861-6_3。

## 3. 具体实现技巧和开发过程

​         景点介绍方面：我在开发的过程中，遇到过很多难点，比如，网站首页如何设计，这么多景点如何罗列，网页点赞的本地保存，以及评论区的实现。在网上寻找到了很多素材后，终于网站有了点好看的模样，但是因为添加的js和css文件太多，出现了文件格式和理想效果不同的问题。后来经过比较玄学的调试，以及重新研究了HTML加载CSS和JS的文件顺序，以及浏览器的渲染过程后，得到了解决了，这里比较坑的在于Chrome因为自带的缓存问题经常不能及时显示你代码中关于CSS的变化，其次js.map文件也延误了改动的生效；再者，js文件link的顺序也会影响有些函数的声明，导致一些函数被覆盖。点赞最后是用比较粗暴的方法实现，存了一个变量来存每个景点对应的变化，没有用对应的数据库存，因为用数据库就必然会涉及到多对一的点赞映射关系，实现上面比较复杂，其次，一般这种数据库的实现都要求用户登录和注册，这种对于旅游网站来说成本太高，不合适，还有就是怎么防止网友刷屏点赞，我们实现过根据IP来限制点赞rate的思路，但是因为游客可能用的是动态IP而不太合适，试过一系列方法，最后发现都存在弊端，所以决定不做限制，这里不得不说的是Django comment的开源包和工具很多，但是很多在用的时候经常和出现环境配置的问题，影响使用。Google识别地图的API的尝试在上面也已经讲明，我们自己尝试实现根据图像相似度匹配来识别景点因为景点的相似度太高，没有特色，以及环境中影响因素太多，干扰了识别的准确度，最后无疾而终。

​     路线规划方面，经过最初的调研，通过比较百度地图api，高德地图api和谷歌地图api3个api所提供的功能。最终根据我们多点步行路径规划的需求，我们选择了谷歌地图API。在经过学习之后，我们将校内的景点通过mark的方式标注在地图上。并且附带链接到介绍页面的超链接。然后通过同样的方式，做了校内活动，食堂，洗手间的位置标注。之后根据谷歌的教程以多项选择的方式来进行景点路径规划。遗憾的是，谷歌也没有提供最优路径规划的功能，所以只能按照既定顺序进行观看。之后在校内活动，食堂，洗手间的位置地图上，我们实现了以点击mark的方式进行从当前定位点进行路径规划的内容。然而，因为是网页版本的定位，所以只能进行不那么精准的ip定位，而且定位安全性能有待加强，以至于有些浏览器不允许进行定位或者定位不够准确等问题的存在，这个希望以后我们能够改进。

​    为了让用户可以更加方便的使用，我们在景点介绍里加入了文字介绍和语音介绍，用户可以直接从地图里选择自己附近的景点，进入景点介绍页面收听我们的录音，我们选择了校园里最具有代表性的十处景点。在API的方面，我们首先想直接利用图像识别来识别出照片上的景点，对比了几个图像识别的API，我们选择了功能强大的谷歌提供的API，但是遗憾的是，这也不能精确的识别出景点，我们的另一个思路是对比照片的相似度（https://huddle.github.io/Resemble.js/）
，把用户拍的照片和我们提供的标准照片进行对比来确定景点。但是由于这种比较主要是基于颜色，形状等，而用户的照片可能有不同的时间、不同的天气、不同的角度，所以这并不能取得一个很好的效果。

## 4. 实验心得和收获

​     喻：总的来说很有收获，第一次做出了有点样子的网站，也基本能够满足用户的以及当初的目标，以后同学来清华也不用自己来带着参观，还是很有成就感，而且网站实现的扩展性也很强，可以在此基础上继续扩大网站的覆盖范围。充分了解了各种强大的API，尤其是Google cloud platform，简直是无所不能，也熟练掌握了利用开放API实现网站功能的能力，对CSS,JS的熟练度也上升了一个档次，对SOA的开发思路和框架有了更加具体的体会。

 	 丁：本次大作业让我认识到了API的强大之处，我们可以通过API轻松地得到大量的地图信息，获取便利的定位服务。使用自己不曾实现的路线规划算法。但是同时，这次大作业也让我认识到了，不能凡事都依赖API，我们因为过于依赖谷歌地图API，和图像识别API导致他们API无法完成的功能，我们也束手无策。所以在学会站在巨人肩膀上的同时，我们也要努力成为巨人的一部分。

​     汪：这次大作业让我学习了很多，第一次做出一个可以供其他人使用的web。在开发的过程中也是对我们原有的设想进行校正，来提高可行性。比如我们最初是想通过二维码进入景点介绍页面，但是为了方便用户选择了拍照，由于我们前面所提到的API功能不足，所以我们最后选择在从地图上直接进入，由于用户不用召唤出摄像头而是直接基于自己的位置找到附近的景点进入介绍页面，其实是更加的方便的。但是我们也存在许多的遗憾，因为考虑到方便用户选择了网页导致牺牲了一部分定位的精准性，希望以后有更好的办法可以改进。

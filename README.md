## Pokemon Data Visualization ##

[Pokemon Stats Kaggle Dataset](https://www.kaggle.com/abcsds/pokemon)

My Kernel
https://www.kaggle.com/edword/d/abcsds/pokemon/stats-comparison-3d-scatter-plot

This dataset includes 721 Pokemon.
The various types of Pokemons in this dataset are:

 1. Grass
 2. Fire 
 3. Water
 4. Dragon
 5. Flying
 6. Steel
 7. Rock
 8. Ice
 9. Electric
 10. Bug
 11. Normal
 12. Ground
 13. Fighting
 14. Ghost
 15. Dark
 16. Psychic
 17. Fairy
 18. Poison

----------
Python Program to analyse the Pokemon Dataset and

 - Plot the average power for each Pokemon type in the form of a Bar chart.
 - 3D Scatter Plot for all Pokemons based on Attack, Defense and HP.

This program makes use of libraries such as:

 - Pandas
 - Matplotlib
 - Numpy
 - mpl_toolkits.mplot3d (Axes3D)


----------
Average Power of each type:

 1. Dragon     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;             550.53125
 2. Grass        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;             421.14285714285717
 3. Ghost        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;             439.5625
 4. Steel         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;              487.7037037037037
 5. Electric     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;               443.40909090909093
 6. Dark          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;               445.741935483871
 7. Rock          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                453.75
 8. Water         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;               430.45535714285717
 9. Normal      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                401.68367346938777
 10. Bug            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;               378.92753623188406
 11. Fighting     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;              416.44444444444446
 12. Fairy          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                 413.1764705882353
 13. Flying        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                  485.0
 14. Poison       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    399.14285714285717
 15. Ice             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    433.4583333333333
 16. Fire           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                     458.0769230769231
 17. Ground      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                      437.5
 18. Psychic       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;475.94736842105266


----------
Colors Used To Represent Pokemon types
http://www.epidemicjohto.com/t882-type-colors-hex-colors

![enter image description here](https://lh3.googleusercontent.com/-rGLDKQikvG8/WOtmLXzUF7I/AAAAAAAABlM/s_NUvFdE4Bc6WFdQDCCwVDP4rg_s6forQCLcB/s0/legend.png "legend.png")

----------



3D Scatter Plot of all Pokemons
-------------------------------

     1. X-axis: Attack
     2. Y-axis: Defense
     3. Z- axis: HP
 
 ![](https://lh3.googleusercontent.com/-HaEPss6ZoLA/WOkuy0jfqxI/AAAAAAAABjY/IT1PtlgN_gYYl39ebuvKatovNhyrg_LdwCLcB/s0/3D.png "3D.png")
 

----------



Comparison Of Attack, Defense, HP and Speed
-------------------------------------------

 

![enter image description here](https://lh3.googleusercontent.com/-i7kxITcW-T4/WOtmbR6wKqI/AAAAAAAABlU/yfhCFLDRsZcNfSrmYP2dEniRPuiTN-YUQCLcB/s0/Main+bar.png "Main bar.png")

----------

 

Average Power comparison
------------------------

 

 - Grass Type, Fire Type and Water Type Pokemons.
![](https://lh3.googleusercontent.com/-lBRYey9Tr_s/WOksg-WEHzI/AAAAAAAABic/ZnYN7osc7MsYLiRIYALN9VGpphTEXjwbQCLcB/s0/figure_1-1.png "figure_1-1.png")


 - Dragon, Flying, Steel, Rock, Ice Type comparison
![](https://lh3.googleusercontent.com/-FavMT9_vBQM/WOktHIn3qpI/AAAAAAAABio/AsinylQFS2kzBeFVLcWs2piKSV3JzG4sQCLcB/s0/figure_2.png "figure_2.png")


 - Electric, Bug, Normal, Ground, Fighting Type comparison
![](https://lh3.googleusercontent.com/-cm2iKVDoo2I/WOkt5TUSqoI/AAAAAAAABi4/MeNPemFYWPomSywWqfF70u_-MjoegOQEgCLcB/s0/figure_3.png "figure_3.png")


 - Ghost, Dark, Psychic, Fairy, Poison Type comparison
![](https://lh3.googleusercontent.com/-i6Cy6Zora_w/WOkuVNWlLhI/AAAAAAAABjA/pXhe4VHbpioa-OQUX1Eu57FK-GeLSjmFwCLcB/s0/figure_4.png "figure_4.png")


----------

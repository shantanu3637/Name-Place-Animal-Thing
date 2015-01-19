#import easygui as eg
#image="tiger.gif"
#text=eg.enterbox("Guess who is in the picture","","","",image,"")
#print text
#lsimage=list(image)
#lsimage=lsimage[0:-4]
#lsimage="".join(lsimage)
#while 1:
#    if text==lsimage:
#        print"nice work"
#        text=eg.enterbox("Guess who is in the picture","","","",image,"")
#    else:
#        print "try again"
#        text=eg.enterbox("Guess who is in the picture","","","",image,"")
#        break


import easygui as eg
import random
class images:
    image=""
    ques_msg=""
    info_msg=""
    
    def get_image(self):
        return self.image
    def get_ques_msg(self):
        return self.ques_msg
    def get_info_msg(self):
        return self.info_msg
    
    
    
obj1=images()
obj1.image="NamePlaceAnimalThing/Lion.gif"
obj1.ques_msg="Name this animal!"
obj1.info_msg="Lions are the second largest big cat species in the world (behind tigers).  The average male lion weighs around 180 kg (400 lb) while the average female lion weighs around 130 kg (290 lb).    The heaviest lion on record weighed an amazing 375 kg (826 lb). Lions can reach speeds of up to 81 kph (50 mph) but only in short bursts because of a lack of stamina.   The roar of a lion can be heard from 8 kilometers (5.0 miles) away."

obj2=images()
obj2.image="NamePlaceAnimalThing/Egypt.gif"
obj2.ques_msg="Name the country in which this famous monument is located."
obj2.info_msg="The pyramids are the stone tombs of Egypt's kings - the Pharaohs and one of the world's greatest historical mysteries. They have stood for thousands of years, filled with many hidden secrets: clues about what life (and death) was like in Ancient Egypt"


obj3=images()
obj3.image="NamePlaceAnimalThing/George.R.R.Martin.gif"
obj3.ques_msg="Name the person in the following picture"
obj3.info_msg="George.r.r.Martin Author of the famous A song of ice and fire series. A tv adaptation of this series currently airs of HBO called the Game of thrones."

obj4=images()
obj4.image="NamePlaceAnimalThing/J.K.Rowling.gif"
obj4.ques_msg="Name the person in the following picture"
obj4.info_msg="J.K.Rowling She is the author of the famous Harry Potter books."

obj5=images()
obj5.image="NamePlaceAnimalThing/Johnny Depp.gif"
obj5.ques_msg="Name the person in the following picture"
obj5.info_msg="Johnny Depp Famous Hollywood actor. He has acted in films like Pirates of Caribbean series, Edward scissorhands etc"

obj6=images()
obj6.image="NamePlaceAnimalThing/Rabindranath Tagore.gif"
obj6.ques_msg="Name the person in the following picture"
obj6.info_msg="Rabindranath Tagore Famous Indian poet, and author. first non-European to win the Nobel Prize in Literature in 1913. Wrote the Indian and Bangladeshi national anthems."

obj7=images()
obj7.image="NamePlaceAnimalThing/Larry Page.gif"
obj7.ques_msg="Name the person in the following picture"
obj7.info_msg="Larry Page. He along with Sergei Brin Co-founded Google. He is currently the Ceo of Google."

obj8=images()
obj8.image="NamePlaceAnimalThing/New Delhi.gif"
obj8.ques_msg="Name the city in which this famous monument is located."
obj8.info_msg="India gate   India Gate is one of the largest war memorials in India.   The monument was designed by Edwin Lutyens, the chief architect of New Delhi.   The foundation stone of India Gate was laid by the Duke of Connaught, on 10th February 1921.    It took approximately 10 years to complete the construction work on the monument, which came to an end in 1931.    The walls of India Gate have been inscribed with the names of the Indian soldiers who died in World War I and the Afghan Wars.    The monument rises to a height of 42 meters and has many important roads spreading out from it.    India Gate also bears some resemblance to the 'Arc de Triomphe', situated in Paris."

obj9=images()
obj9.image="NamePlaceAnimalThing/New York.gif"
obj9.ques_msg="Name the city in which this famous monument is located."
obj9.info_msg="Statue of liberty The Statue of Liberty celebrates her birthday on October 28th in honor of the day she was officially accepted by the president of the United States in 1886. Visitors must climb 354 stairs to reach the Statue of Liberty's crown (or take an elevator to a lower lookout point).  There are 25 windows in Lady Liberty's crown.  The seven spikes on the Statue of Liberty's crown represent either the seven oceans or the seven continents.  The statue is made of copper and is now green in color because of oxidation (a chemical reaction between metal and water) from evaporation of the seawater surrounding it"

obj10=images()
obj10.image="NamePlaceAnimalThing/Paris.gif"
obj10.ques_msg="Name the city in which this famous monument is located."
obj10.info_msg="Eiffel tower   Located on the Champ de Mars in Paris, France, the Eiffel Tower is one of the most well known structures in the world.    The Eiffel Tower was originally built as the entrance arch for the World's Fair in 1889.  It is named after Gustave Eiffel, whose company was in charge of the project.    The Eiffel Tower is 320 metres (1050 feet) in height and was the tallest man made structure in the world for 41 years before being surpassed by the Chrysler Building in New York.    The Eiffel Tower is made of iron and weighs around 10000 tonnes."

obj11=images()
obj11.image="NamePlaceAnimalThing/Agra.gif"
obj11.ques_msg="Name the city in which this famous monument is located."
obj11.info_msg="Taj Mahal    It is estimated to have taken more than 22,000 people to build this impressive building including labourers, painters, stonecutters, embroidery artists, and many others.According to legend it is believed that Emperor Shah Jahan had planned to construct another Taj Mahal in black marble on the other side of the river but the war with his sons interrupted his plans.3.    The Taj Mahal takes on different colouring at different times of the day, from a pinkish hue in the morning, milky white in the evening and golden at night when lit by the moon. They say the changing colour resembles the changing mood of females - in particular the Emperor's queen.4.    Built in memory of the Emperors third and most favourite wife Mumtaz Mahal, the Taj Mahal took 17 years to be completed.5.    It is said that the death so crushed the Emperor that all his hair and beard were said to have grown snow white within just a few months."

obj12=images()
obj12.image="NamePlaceAnimalThing/guitar.gif"
obj12.ques_msg="Identify the thing shown in the picture"
obj12.info_msg="Guitar. Guitar is one of the most popular musical instruments in the world. Many popular artists including The Beatles  have used the guitar."

obj13=images()
obj13.image="NamePlaceAnimalThing/screwdriver.gif"
obj13.ques_msg="Identify the thing shown in the picture"
obj13.info_msg="Screwdriver.This is an appliance used to fix screws."

obj14=images()
obj14.image="NamePlaceAnimalThing/table lamp.gif"
obj14.ques_msg="Identify the thing shown in the picture"
obj14.info_msg="Table lamp.Table lamp is used to illuminate study tables."

obj15=images()
obj15.image="NamePlaceAnimalThing/alarm clock.gif"
obj15.ques_msg="Identify the thing shown in the picture"
obj15.info_msg="Alarm clock. Alarm clocks are used to wake up on time."

obj16=images()
obj16.image="NamePlaceAnimalThing/umbrella.gif"
obj16.ques_msg="Identify the thing shown in the picture"
obj16.info_msg="Umbrella.Umbrella is used to protect ourselves  from rain."

obj17=images()
obj17.image="NamePlaceAnimalThing/Tiger.gif"
obj17.ques_msg="Name this animal!"
obj17.info_msg="The tiger is the biggest species of the cat family.Tigers can reach a length of up to 3.3 metres (11 feet) and weigh as much as 300 kilograms (660 pounds).Subspecies of the tiger include the Sumatran Tiger, Siberian Tiger, Bengal Tiger, South China Tiger, Malayan Tiger and Indochinese Tiger.Many subspecies of the tiger are either endangered or already extinct.Humans are the primary cause of this through hunting and the destruction of habitats.Around half of tiger cubs dont live beyond two years of age."

obj18=images()
obj18.image="NamePlaceAnimalThing/Kangaroo.gif"
obj18.ques_msg="Name this animal!"
obj18.info_msg="Kangaroos are marsupial animals that are found in Australia as well as New Guinea.There are four different kangaroo species, the red kangaroo, eastern grey kangaroo, western grey kangaroo and antilopine kangaroo.Kangaroos can hop around quickly on two legs or walk around slowly on all four.Kangaroos cant walk backwards.Kangaroos have very powerful legs and can be dangerous at times."

obj19=images()
obj19.image="NamePlaceAnimalThing/Polar bear.gif"
obj19.ques_msg="Name this animal!"
obj19.info_msg="Polar bears live in the Arctic.Polar bears have black fur under their outer layer of white fur.It is the largest carnivore (meat eater) that lives on land.Polar bears use sea ice as a platform to hunt seals.Seals make up most of a polar bears diet."

obj20=images()
obj20.image="NamePlaceAnimalThing/Mammoth.gif"
obj20.ques_msg="Name this animal!"
obj20.info_msg="The word Mammoth comes from two words from the Estonian language: Maa, which means earth, and Mutt, which means mole. The mammoth is a relative to the modern elephant (Proboscidea).Like many other Ice Age mammals, the mammoth became extinct more than 11,000 years ago."

obj21=images()
obj21.image="NamePlaceAnimalThing/Parrot.gif"
obj21.ques_msg="Name this bird!"
obj21.info_msg=" There are around 372 different parrot species.Most parrots live in tropical areas.Parrots have curved bills (beaks), strong legs and clawed feet.    Parrots are often brightly coloured.Parrots are believed to be one of the most intelligent bird species"

variable=[obj1,obj2,obj3,obj4,obj5,obj6,obj7,obj8,obj9,obj10,obj11,obj12,obj13,obj14,obj15,obj16,obj17,obj18,obj19,obj20,obj21]

boolean=True

while(boolean==True):
    

    i=random.randrange(0,21,1)
    
    lsimage=list(variable[i].get_image())
    lsimage=lsimage[0:-4]
    lsimage="".join(lsimage)
    
    text=eg.enterbox(variable[i].get_ques_msg(),"","","",variable[i].get_image(),"")
    
    if text==None:
        break
    
        
    if lsimage==text:
        ans="Correct!                                                                                                                                                                                                  "                                                                                                                                
    else:
        ans="Wrong!                                                                                                                                                                                                     "
                                                                                                                                                                                                                
    
    choice=eg.buttonbox(ans+variable[i].get_info_msg(),"",("Continue","exit"),variable[i].get_image(),"")
    if choice=="Continue":
        pass
    else:
        boolean= False
    
    

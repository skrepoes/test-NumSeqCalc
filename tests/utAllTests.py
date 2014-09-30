# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UtAllTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = ""
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_ut_alltests(self):
        driver = self.driver
        driver.get(self.base_url + "file:///C:/NumSeqCalc/wwwroot/index.html")
        
        driver.get(self.base_url + "file:///C:/NumSeqCalc/wwwroot/index.html")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        time.sleep(1)
        driver.find_element_by_css_selector("button.close").click()
        time.sleep(1)
        
        driver.find_element_by_id("calcData").clear()
        driver.find_element_by_id("calcData").send_keys("")
        driver.find_element_by_id("calcSubmit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#calcError").text, r"^[\s\S]*Please enter a positive number\.[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        time.sleep(1)
        
        driver.find_element_by_id("calcData").clear()
        driver.find_element_by_id("calcData").send_keys("0")
        driver.find_element_by_id("calcSubmit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#calcError").text, r"^[\s\S]*Please enter a positive number\.[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        time.sleep(1)

        driver.find_element_by_id("calcData").clear()
        driver.find_element_by_id("calcData").send_keys("text")
        driver.find_element_by_id("calcSubmit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#calcError").text, r"^[\s\S]*Please enter a positive number\.[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        time.sleep(1)            
            
        driver.find_element_by_id("calcData").clear()
        driver.find_element_by_id("calcData").send_keys("1")
        driver.find_element_by_id("calcSubmit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsMultis").text, r"^[\s\S]*1[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsOdds").text, r"^[\s\S]*1[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsEvens").text, r"^[\s\S]*No even numbers[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))  
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsMultis").text, r"^[\s\S]*1[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))   
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsFibo").text, r"^[\s\S]*0, 1, 1[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e)) 
        time.sleep(1)    
        
        driver.find_element_by_id("calcData").clear()
        driver.find_element_by_id("calcData").send_keys("10")
        driver.find_element_by_id("calcSubmit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsSeq").text, r"^[\s\S]*1, 2, 3, 4, 5, 6, 7, 8, 9, 10[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsOdds").text, r"^[\s\S]*1, 3, 5, 7, 9[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsEvens").text, r"^[\s\S]*2, 4, 6, 8, 10[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))  
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsMultis").text, r"^[\s\S]*1, 2, C, 4, E, C, 7, 8, C, E[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))   
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsFibo").text, r"^[\s\S]*0, 1, 1, 2, 3, 5, 8[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e)) 
        time.sleep(1)               
            
        driver.find_element_by_id("calcData").clear()
        driver.find_element_by_id("calcData").send_keys("100")
        driver.find_element_by_id("calcSubmit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsSeq").text, r"^[\s\S]*1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsOdds").text, r"^[\s\S]*1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsEvens").text, r"^[\s\S]*2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))  
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsMultis").text, r"^[\s\S]*1, 2, C, 4, E, C, 7, 8, C, E, 11, C, 13, 14, Z, 16, 17, C, 19, E, C, 22, 23, C, E, 26, C, 28, 29, Z, 31, 32, C, 34, E, C, 37, 38, C, E, 41, C, 43, 44, Z, 46, 47, C, 49, E, C, 52, 53, C, E, 56, C, 58, 59, Z, 61, 62, C, 64, E, C, 67, 68, C, E, 71, C, 73, 74, Z, 76, 77, C, 79, E, C, 82, 83, C, E, 86, C, 88, 89, Z, 91, 92, C, 94, E, C, 97, 98, C, E[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))   
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsFibo").text, r"^[\s\S]*0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))   
        time.sleep(1)            

            
        driver.find_element_by_id("calcData").clear()
        driver.find_element_by_id("calcData").send_keys("1000")
        driver.find_element_by_id("calcSubmit").click()
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsSeq").text, r"^[\s\S]*1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsOdds").text, r"^[\s\S]*1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199, 201, 203, 205, 207, 209, 211, 213, 215, 217, 219, 221, 223, 225, 227, 229, 231, 233, 235, 237, 239, 241, 243, 245, 247, 249, 251, 253, 255, 257, 259, 261, 263, 265, 267, 269, 271, 273, 275, 277, 279, 281, 283, 285, 287, 289, 291, 293, 295, 297, 299, 301, 303, 305, 307, 309, 311, 313, 315, 317, 319, 321, 323, 325, 327, 329, 331, 333, 335, 337, 339, 341, 343, 345, 347, 349, 351, 353, 355, 357, 359, 361, 363, 365, 367, 369, 371, 373, 375, 377, 379, 381, 383, 385, 387, 389, 391, 393, 395, 397, 399, 401, 403, 405, 407, 409, 411, 413, 415, 417, 419, 421, 423, 425, 427, 429, 431, 433, 435, 437, 439, 441, 443, 445, 447, 449, 451, 453, 455, 457, 459, 461, 463, 465, 467, 469, 471, 473, 475, 477, 479, 481, 483, 485, 487, 489, 491, 493, 495, 497, 499, 501, 503, 505, 507, 509, 511, 513, 515, 517, 519, 521, 523, 525, 527, 529, 531, 533, 535, 537, 539, 541, 543, 545, 547, 549, 551, 553, 555, 557, 559, 561, 563, 565, 567, 569, 571, 573, 575, 577, 579, 581, 583, 585, 587, 589, 591, 593, 595, 597, 599, 601, 603, 605, 607, 609, 611, 613, 615, 617, 619, 621, 623, 625, 627, 629, 631, 633, 635, 637, 639, 641, 643, 645, 647, 649, 651, 653, 655, 657, 659, 661, 663, 665, 667, 669, 671, 673, 675, 677, 679, 681, 683, 685, 687, 689, 691, 693, 695, 697, 699, 701, 703, 705, 707, 709, 711, 713, 715, 717, 719, 721, 723, 725, 727, 729, 731, 733, 735, 737, 739, 741, 743, 745, 747, 749, 751, 753, 755, 757, 759, 761, 763, 765, 767, 769, 771, 773, 775, 777, 779, 781, 783, 785, 787, 789, 791, 793, 795, 797, 799, 801, 803, 805, 807, 809, 811, 813, 815, 817, 819, 821, 823, 825, 827, 829, 831, 833, 835, 837, 839, 841, 843, 845, 847, 849, 851, 853, 855, 857, 859, 861, 863, 865, 867, 869, 871, 873, 875, 877, 879, 881, 883, 885, 887, 889, 891, 893, 895, 897, 899, 901, 903, 905, 907, 909, 911, 913, 915, 917, 919, 921, 923, 925, 927, 929, 931, 933, 935, 937, 939, 941, 943, 945, 947, 949, 951, 953, 955, 957, 959, 961, 963, 965, 967, 969, 971, 973, 975, 977, 979, 981, 983, 985, 987, 989, 991, 993, 995, 997, 999[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsEvens").text, r"^[\s\S]*2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 254, 256, 258, 260, 262, 264, 266, 268, 270, 272, 274, 276, 278, 280, 282, 284, 286, 288, 290, 292, 294, 296, 298, 300, 302, 304, 306, 308, 310, 312, 314, 316, 318, 320, 322, 324, 326, 328, 330, 332, 334, 336, 338, 340, 342, 344, 346, 348, 350, 352, 354, 356, 358, 360, 362, 364, 366, 368, 370, 372, 374, 376, 378, 380, 382, 384, 386, 388, 390, 392, 394, 396, 398, 400, 402, 404, 406, 408, 410, 412, 414, 416, 418, 420, 422, 424, 426, 428, 430, 432, 434, 436, 438, 440, 442, 444, 446, 448, 450, 452, 454, 456, 458, 460, 462, 464, 466, 468, 470, 472, 474, 476, 478, 480, 482, 484, 486, 488, 490, 492, 494, 496, 498, 500, 502, 504, 506, 508, 510, 512, 514, 516, 518, 520, 522, 524, 526, 528, 530, 532, 534, 536, 538, 540, 542, 544, 546, 548, 550, 552, 554, 556, 558, 560, 562, 564, 566, 568, 570, 572, 574, 576, 578, 580, 582, 584, 586, 588, 590, 592, 594, 596, 598, 600, 602, 604, 606, 608, 610, 612, 614, 616, 618, 620, 622, 624, 626, 628, 630, 632, 634, 636, 638, 640, 642, 644, 646, 648, 650, 652, 654, 656, 658, 660, 662, 664, 666, 668, 670, 672, 674, 676, 678, 680, 682, 684, 686, 688, 690, 692, 694, 696, 698, 700, 702, 704, 706, 708, 710, 712, 714, 716, 718, 720, 722, 724, 726, 728, 730, 732, 734, 736, 738, 740, 742, 744, 746, 748, 750, 752, 754, 756, 758, 760, 762, 764, 766, 768, 770, 772, 774, 776, 778, 780, 782, 784, 786, 788, 790, 792, 794, 796, 798, 800, 802, 804, 806, 808, 810, 812, 814, 816, 818, 820, 822, 824, 826, 828, 830, 832, 834, 836, 838, 840, 842, 844, 846, 848, 850, 852, 854, 856, 858, 860, 862, 864, 866, 868, 870, 872, 874, 876, 878, 880, 882, 884, 886, 888, 890, 892, 894, 896, 898, 900, 902, 904, 906, 908, 910, 912, 914, 916, 918, 920, 922, 924, 926, 928, 930, 932, 934, 936, 938, 940, 942, 944, 946, 948, 950, 952, 954, 956, 958, 960, 962, 964, 966, 968, 970, 972, 974, 976, 978, 980, 982, 984, 986, 988, 990, 992, 994, 996, 998, 1000[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))  
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsMultis").text, r"^[\s\S]*1, 2, C, 4, E, C, 7, 8, C, E, 11, C, 13, 14, Z, 16, 17, C, 19, E, C, 22, 23, C, E, 26, C, 28, 29, Z, 31, 32, C, 34, E, C, 37, 38, C, E, 41, C, 43, 44, Z, 46, 47, C, 49, E, C, 52, 53, C, E, 56, C, 58, 59, Z, 61, 62, C, 64, E, C, 67, 68, C, E, 71, C, 73, 74, Z, 76, 77, C, 79, E, C, 82, 83, C, E, 86, C, 88, 89, Z, 91, 92, C, 94, E, C, 97, 98, C, E, 101, C, 103, 104, Z, 106, 107, C, 109, E, C, 112, 113, C, E, 116, C, 118, 119, Z, 121, 122, C, 124, E, C, 127, 128, C, E, 131, C, 133, 134, Z, 136, 137, C, 139, E, C, 142, 143, C, E, 146, C, 148, 149, Z, 151, 152, C, 154, E, C, 157, 158, C, E, 161, C, 163, 164, Z, 166, 167, C, 169, E, C, 172, 173, C, E, 176, C, 178, 179, Z, 181, 182, C, 184, E, C, 187, 188, C, E, 191, C, 193, 194, Z, 196, 197, C, 199, E, C, 202, 203, C, E, 206, C, 208, 209, Z, 211, 212, C, 214, E, C, 217, 218, C, E, 221, C, 223, 224, Z, 226, 227, C, 229, E, C, 232, 233, C, E, 236, C, 238, 239, Z, 241, 242, C, 244, E, C, 247, 248, C, E, 251, C, 253, 254, Z, 256, 257, C, 259, E, C, 262, 263, C, E, 266, C, 268, 269, Z, 271, 272, C, 274, E, C, 277, 278, C, E, 281, C, 283, 284, Z, 286, 287, C, 289, E, C, 292, 293, C, E, 296, C, 298, 299, Z, 301, 302, C, 304, E, C, 307, 308, C, E, 311, C, 313, 314, Z, 316, 317, C, 319, E, C, 322, 323, C, E, 326, C, 328, 329, Z, 331, 332, C, 334, E, C, 337, 338, C, E, 341, C, 343, 344, Z, 346, 347, C, 349, E, C, 352, 353, C, E, 356, C, 358, 359, Z, 361, 362, C, 364, E, C, 367, 368, C, E, 371, C, 373, 374, Z, 376, 377, C, 379, E, C, 382, 383, C, E, 386, C, 388, 389, Z, 391, 392, C, 394, E, C, 397, 398, C, E, 401, C, 403, 404, Z, 406, 407, C, 409, E, C, 412, 413, C, E, 416, C, 418, 419, Z, 421, 422, C, 424, E, C, 427, 428, C, E, 431, C, 433, 434, Z, 436, 437, C, 439, E, C, 442, 443, C, E, 446, C, 448, 449, Z, 451, 452, C, 454, E, C, 457, 458, C, E, 461, C, 463, 464, Z, 466, 467, C, 469, E, C, 472, 473, C, E, 476, C, 478, 479, Z, 481, 482, C, 484, E, C, 487, 488, C, E, 491, C, 493, 494, Z, 496, 497, C, 499, E, C, 502, 503, C, E, 506, C, 508, 509, Z, 511, 512, C, 514, E, C, 517, 518, C, E, 521, C, 523, 524, Z, 526, 527, C, 529, E, C, 532, 533, C, E, 536, C, 538, 539, Z, 541, 542, C, 544, E, C, 547, 548, C, E, 551, C, 553, 554, Z, 556, 557, C, 559, E, C, 562, 563, C, E, 566, C, 568, 569, Z, 571, 572, C, 574, E, C, 577, 578, C, E, 581, C, 583, 584, Z, 586, 587, C, 589, E, C, 592, 593, C, E, 596, C, 598, 599, Z, 601, 602, C, 604, E, C, 607, 608, C, E, 611, C, 613, 614, Z, 616, 617, C, 619, E, C, 622, 623, C, E, 626, C, 628, 629, Z, 631, 632, C, 634, E, C, 637, 638, C, E, 641, C, 643, 644, Z, 646, 647, C, 649, E, C, 652, 653, C, E, 656, C, 658, 659, Z, 661, 662, C, 664, E, C, 667, 668, C, E, 671, C, 673, 674, Z, 676, 677, C, 679, E, C, 682, 683, C, E, 686, C, 688, 689, Z, 691, 692, C, 694, E, C, 697, 698, C, E, 701, C, 703, 704, Z, 706, 707, C, 709, E, C, 712, 713, C, E, 716, C, 718, 719, Z, 721, 722, C, 724, E, C, 727, 728, C, E, 731, C, 733, 734, Z, 736, 737, C, 739, E, C, 742, 743, C, E, 746, C, 748, 749, Z, 751, 752, C, 754, E, C, 757, 758, C, E, 761, C, 763, 764, Z, 766, 767, C, 769, E, C, 772, 773, C, E, 776, C, 778, 779, Z, 781, 782, C, 784, E, C, 787, 788, C, E, 791, C, 793, 794, Z, 796, 797, C, 799, E, C, 802, 803, C, E, 806, C, 808, 809, Z, 811, 812, C, 814, E, C, 817, 818, C, E, 821, C, 823, 824, Z, 826, 827, C, 829, E, C, 832, 833, C, E, 836, C, 838, 839, Z, 841, 842, C, 844, E, C, 847, 848, C, E, 851, C, 853, 854, Z, 856, 857, C, 859, E, C, 862, 863, C, E, 866, C, 868, 869, Z, 871, 872, C, 874, E, C, 877, 878, C, E, 881, C, 883, 884, Z, 886, 887, C, 889, E, C, 892, 893, C, E, 896, C, 898, 899, Z, 901, 902, C, 904, E, C, 907, 908, C, E, 911, C, 913, 914, Z, 916, 917, C, 919, E, C, 922, 923, C, E, 926, C, 928, 929, Z, 931, 932, C, 934, E, C, 937, 938, C, E, 941, C, 943, 944, Z, 946, 947, C, 949, E, C, 952, 953, C, E, 956, C, 958, 959, Z, 961, 962, C, 964, E, C, 967, 968, C, E, 971, C, 973, 974, Z, 976, 977, C, 979, E, C, 982, 983, C, E, 986, C, 988, 989, Z, 991, 992, C, 994, E, C, 997, 998, C, E[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))   
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("#numsFibo").text, r"^[\s\S]*0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e)) 
        time.sleep(1)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

import random

Micro_token = ["AditiChaubey_Gen", "BhumikaGoyal_Gen", "DaulatKadam_Gen", "DolishJain_Gen", "BrijeshG_Gen", "Harsh_Gen", "JiyaChauhan_Gen", "Krishna_Gen", "LamnganbiChingangbam_Gen", "MedhaAgarwal_Gen", "Mohit_Gen", "Raman_Gen", "SanikaJogalekar_Gen", "SanjushriGore_Gen", "ShailySengar_Gen", "ShantanuDravid_Gen", "ShishankSharma_Gen", "ShoumiChatterjee_Gen", "ShubhArora_Gen", "SnehaMathew_Gen", "TanushreeKannan_Gen", "VidhiTaneja_Gen", "ViratRawat_Gen", "Vishant_Gen", "Yashwardhan_Gen", "Tanya_Gen", "MissingPerson1_Gen"]
Agri_token = ["AdyasaAuroprava_Agri", "AnushkaSingh_Agri", "ArinGupta_Agri", "Ashok_Agri", "AthulCyriacRoy_Agri", "AvishiRaviDutt_Agri", "Ayantika_Agri", "Bharati_Agri", "Missingperson1_Agri", "DevangiMazumder_Agri", "DibyaBhowmik_Agri", "EbiBiju_Agri", "HarshitaKumari_Agri", "HarshitaSharma_Agri", "JahanaviSharma_Agri", "JoannaMariaJohn_Agri", "GayatriTayade_Agri", "JuhiBhuyan_Agri", "KarthikKS_Agri", "MansiAgrawal_Agri", "ManyataGupta_Agri", "MuskaanBhatia_Agri", "Vanshika_Agri", "NaveenTayal_Agri", "NivelJoy_Agri", "OmkarMahapatra_Agri", "PrachetaDas_Agri", "Prathamesh_Agri", "Missingperson2_Agri", "RituChaudhary_Agri", "RiyaMaryGeorge_Agri", "RuchiMunot_Agri", "Saptaparno_Agri", "AmanShukla_Agri", "SrijaniMitra_Agri", "PrarthanaChilka_Agri", "Vomika_Agri"]
Geopolitics_token = ["Aditya_Geo", "Amisha_Geo", "Ann_Geo", "Antariya_Geo", "Anusha_Geo", "Anushka_Geo", "Aravindha_Geo", "Chitsa_Geo", "Diptangshu_Geo", "Gagandeep_Geo", "Jayti_Geo", "Jimona_Geo", "Kirtivardhan_Geo", "Parneet_Geo", "Pramit_Geo", "Preet_Geo", "Ritobhash_Geo", "Sahana_Geo", "Saif_Geo", "Sanghamitra_Geo", "Sharvi_Geo", "ShibaPrasad_Geo", "Snehal_Geo", "Shreyas_Geo", "Utsav_Geo", "Vidhi_Geo"]

final_222 = []
final_232 = []
final_131 = []
final_231 = []

def pick_random(l):
    a = random.choice(l)
    l.remove(a)
    return a

def insert_elements(n, l1, l2):
    for i in range(0, n):
        l1.append(pick_random(l2))
    return l1

n1, n2, n3, n4 = 0, 0, 0, 0

while n1 < 7:
    list_group_222 = []
    list_group_222 = insert_elements(2, list_group_222, Micro_token)
    list_group_222 = insert_elements(2, list_group_222, Agri_token)
    list_group_222 = insert_elements(2, list_group_222, Geopolitics_token)
    final_222.append(list_group_222)
    n1 += 1

while n2 < 5:
    list_group_232 = []
    list_group_232 = insert_elements(2, list_group_232, Micro_token)
    list_group_232 = insert_elements(3, list_group_232, Agri_token)
    list_group_232 = insert_elements(2, list_group_232, Geopolitics_token)
    final_232.append(list_group_232)
    n2 += 1

list_group_131 = []
list_group_131 = insert_elements(1, list_group_131, Micro_token)
list_group_131 = insert_elements(3, list_group_131, Agri_token)
list_group_131 = insert_elements(1, list_group_131, Geopolitics_token)
final_131.append(list_group_131)

list_group_231 = []
list_group_231 = insert_elements(2, list_group_231, Micro_token)
list_group_231 = insert_elements(3, list_group_231, Agri_token)
list_group_231 = insert_elements(1, list_group_231, Geopolitics_token)
final_231.append(list_group_231)

group_counter = 1

for group in final_222:
    print("Group " + str(group_counter) + " : " + '\t'.join(group))
    group_counter += 1

for group in final_232:
    print("Group " + str(group_counter) + " : " + '\t'.join(group))
    group_counter += 1

print("Group " + str(group_counter) + " : " + '\t'.join(final_131[0]))
group_counter += 1

print("Group " + str(group_counter) + " : " + '\t'.join(final_231[0]))

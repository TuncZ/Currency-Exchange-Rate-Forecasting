load fisheriris
%% dataları görselleştirme
f= figure;
gscatter(meas(:,3),meas(:,4),species,'rgb','osd');
xlabel('petal uzunlugu');
 ylabel('petal genisligi')
 %%random sayı ayarlıyoruz 
 rand_num=randperm(150);
 %%satıları random dağıtacak train ve testler
 Train_Data_Meas  = meas(rand_num(1:120),3:4);
 Train_Data_Species = species(rand_num(1:120),:);
 Test_Data_Meas  = meas(rand_num(121:end),3:4);
Test_Data_Species = species(rand_num(121:end),1);
 %% linearSVM modeli fitcecoc fonksiyonuyla eğitiyoruz
 Mdl = fitcecoc(Train_Data_Meas,Train_Data_Species);
 %%Denem aşaması
 tahmin_edilen=predict(Mdl,Test_Data_Meas);
%%Karşılaştırm aşaması
 karsilastirma = strcmp(tahmin_edilen,Test_Data_Species);
 %%Doğruluk oranı hesaplıyoruz
 toplam=0;
test_data_sayisi=30;
 for i =1:30
 toplam=toplam+karsilastirma(i);
end
dogru_bulma_orani=toplam*100/test_data_sayisi
 %% matris çizdirme
d=figure
 cm = confusionchart(Test_Data_Species,tahmin_edilen);


% Import data
for i=1:198 %last column (199) does not have enough samples
    rmBrackets = 'sed ''s/\[//g;s/\]//g'' letterdata';
    system([rmBrackets, [int2str(i*100) ' >> tmp']])
    raw = importdata('tmp');
    error(:,i) = raw(:,2)./(raw(:,1)+raw(:,2))
    system('rm tmp');
end

% Plot Results

figure(1);
subplot(2,1,1)
hold on
%TODO: Shade between lines rather than dotted lines
plot(mean(error)+std(error), '-k');
plot(mean(error)-std(error), '-k');
plot(mean(error))
title('Error with increasing Training/Test Ratio')

meanError = mean(error(:,[40:end]),2);
subplot(2,1,2)
bar(meanError)
set(gca,'Xtick',[1:26])
set(gca,'XTickLabel',{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'...
                    , 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'...
                    , 'u', 'v', 'w', 'x', 'y', 'z'});
hold on;
h=errorbar([1:26], meanError, std(error(:,[40:end]),1,2));
set(h,'linestyle','none', 'color', 'r');
axis([0 27 0 0.45])
title('Mean Letter Error Rates (after 20% Training mix)')


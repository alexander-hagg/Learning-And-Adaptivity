
% Import data
for i=1:198 %last column (199) does not have enough samples
    rmBrackets = 'sed ''s/\[//g;s/\]//g'' letterdata';
    system([rmBrackets, [int2str(i*100) ' >> tmp']])
    raw = importdata('tmp');
    error(:,i) = raw(:,2)./(raw(:,1)+raw(:,2))
    system('rm tmp');
end

% Plot Results
figure(1);clf;
    subplot(3,1,1)
        hold on
        %TODO: Shade between lines rather than dotted lines
        x = linspace(1,198,198);
        mean_error = mean(error);
        mean_plus_std = mean(error)+std(error);
        mean_minus_std = mean(error)-std(error);
        fill( [x fliplr(x)],  [mean_plus_std fliplr(mean_minus_std)], 'b');
        alpha(.05);
        plot(x, mean_error, 'k', 'LineWidth', 2)
        plot(x, mean_plus_std, 'b')
        legend('StdDev','Mean')
        plot(x, mean_minus_std, 'b')

        title('Error', 'FontSize', 14)
        set(gca,'XTickLabel',{'0%', '10%', '20%', '30%', '40%', '50%'...
                            , '60%', '70%', '80%', '90%', '100%'});
        xlabel('Percent of Total Data used for Training')
        ylabel('Error on Test Set')
        

    subplot(3,1,2)
        time = importdata('timefile');
        plot(x,time([1:198],2));
        title('Training Time', 'FontSize', 14)
        set(gca,'XTickLabel',{'0%', '10%', '20%', '30%', '40%', '50%'...
                            , '60%', '70%', '80%', '90%', '100%'});
        xlabel('Percent of Total Data used for Training')
        ylabel('Seconds')

    subplot(3,1,3)
        hold on
        tree_size = importdata('treesize');
        plot(x,tree_size([1:198],2));
        title('Tree Size', 'FontSize', 14)
        set(gca,'XTickLabel',{'0%', '10%', '20%', '30%', '40%', '50%'...
                            , '60%', '70%', '80%', '90%', '100%'});
        xlabel('Percent of Total Data used for Training')
        ylabel('Nodes')


figure(2)
    meanError = mean(error(:,[40:end]),2);
    bar(meanError)
    set(gca,'Xtick',[1:26])
    set(gca,'XTickLabel',{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'...
                        , 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'...
                        , 'u', 'v', 'w', 'x', 'y', 'z'});
    hold on;
    h=errorbar([1:26], meanError, std(error(:,[40:end]),1,2));
    set(h,'linestyle','none', 'color', 'r');
    axis([0 27 0 0.30])
    title('Mean Letter Error Rates (20% to 95% Training mix)', 'FontSize', 14)


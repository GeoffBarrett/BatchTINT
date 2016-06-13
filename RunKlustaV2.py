# import os, read_data, json, subprocess
import os, json, subprocess, time, datetime

class runKlusta():

    def __init__(self):
        super(runKlusta, self).__init__()

    def klusta(self, expt, directory):
        cur_time = datetime.datetime.now().time()
        folder_msg = ': Now analyzing files in the "' + expt + '" folder!'
        print(str(cur_time)[:8] + folder_msg)

        dir_new = os.path.join(directory, expt)  # makes a new directory

        self.settings_fname = 'settings.json'

        with open(self.settings_fname, 'r+') as filename:
            self.settings = json.load(filename)

        f_list = os.listdir(dir_new)  # finds the files within that directory
        set_file = [file for file in f_list if '.set' in file]
        set_file = set_file[0][:-3]
        set_path = os.path.join(dir_new, set_file[:-1])

        tet_list = [file for file in f_list if file in ['%s%d' % (set_file, i)
                                                        for i in range(1, int(self.settings['NumTet']) + 1)]]

        if tet_list == []:
            cur_time = datetime.datetime.now().time()
            no_files_msg = ': There are no files that need analyzing in the "' + expt + '" folder!'
            print(str(cur_time)[:8] + no_files_msg)
        else:
            # print(tet_list)
            for tet_fname in tet_list:

                for i in range(1, int(self.settings['NumTet']) + 1):
                    if ['%s%d' % ('.', i) in tet_fname][0]:
                        tetrode = i

                cur_time = datetime.datetime.now().time()
                file_analyze_msg = ': Now analyzing the following file: ' + tet_fname
                print(str(cur_time)[:8] + file_analyze_msg)

                clu_name = set_path + '.clu.' + str(tetrode)
                cut_path = set_path + '_' + str(tetrode) + '.cut'
                cut_name = set_file[:-1] + '_' + str(tetrode) + '.cut'

                if cut_name in f_list:
                    already_done = 'The ' + set_file[:-1] + ' has already been analyzed, skipping!'
                    print(already_done)
                    continue

                tet_path = os.path.join(dir_new, tet_fname)  # adding a .prm at the end will be the same as the PRM file

                ini_fname = tet_path + '.ini'

                parm_space = ' '
                kkparmstr = parm_space.join(['-MaxPossibleClusters', str(self.settings['MaxPos']),
                                             '-nStarts', str(self.settings['nStarts']),
                                            '-RandomSeed', str(self.settings['RandomSeed']),
                                             '-DistThresh', str(self.settings['DistThresh']),
                                             '-FullStepEvery', str(self.settings['FullStepEvery']),
                                             '-ChangedThresh', str(self.settings['ChangedThresh']),
                                             '-MaxIter', str(self.settings['MaxIter']),
                                             '-SplitEvery', str(self.settings['SplitEvery']),
                                             '-Subset', str(self.settings['Subset']),
                                             '-PenaltyK', str(self.settings['PenaltyK']),
                                             '-PenaltyKLogN', str(self.settings['PenaltyKLogN']),
                                             '-UseDistributional', '1',
                                             '-UseMaskedInitialConditions', '1',
                                             '-AssignToFirstClosestMask', '1',
                                             '-PriorPoint', '1',
                                             ])
                s = "\n"
                inc_channels = s.join(['[IncludeChannels]',
                                       '1=' + str(self.settings['1']),
                                       '2=' + str(self.settings['2']),
                                       '3=' + str(self.settings['3']),
                                       '4=' + str(self.settings['4'])
                                       ])

                with open(ini_fname, 'w') as fname:

                    s = "\n"
                    main_seq = s.join(['[Main]',
                                       str('Filename=' + '"' + set_path + '"'),
                                       str('IDnumber=' + str(tetrode)),
                                       str('KKparamstr=' + kkparmstr),
                                       str(inc_channels)
                                       ])


                    clust_ft_seq = s.join(['\n[ClusteringFeatures]',
                                           str('PC1=' + str(self.settings['PC1'])),
                                           str('PC2=' + str(self.settings['PC2'])),
                                           str('PC3=' + str(self.settings['PC3'])),
                                           str('PC4=' + str(self.settings['PC4'])),
                                           str('A=' + str(self.settings['A'])),
                                           str('Vt=' + str(self.settings['Vt'])),
                                           str('P=' + str(self.settings['P'])),
                                           str('T=' + str(self.settings['T'])),
                                           str('tP=' + str(self.settings['tP'])),
                                           str('tT=' + str(self.settings['tT'])),
                                           str('En=' + str(self.settings['En'])),
                                           str('Ar=' + str(self.settings['Ar']))
                                           ])

                    report_seq = s.join(['\n[Reporting]',
                                         'Log=' + str(self.settings['Log File']),
                                        'Verbose=' + str(self.settings['Verbose']),
                                         'Screen=' + str(self.settings['Screen'])
                                         ])

                    for write_order in [main_seq, clust_ft_seq, report_seq]:
                        fname.seek(0, 2)  # seek the files end
                        fname.write(write_order)

                log_fname = tet_path + '_log.txt'

                cmdline = ["cmd", "/q", "/k", "echo off"]

                cmd = subprocess.Popen(cmdline, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

                # batch = []
                batch = bytes(
                    'tint ' + '"' + set_path + '" ' + str(tetrode) + ' "' + log_fname + '" /runKK /KKoptions "' +
                    ini_fname + '"\n', 'ascii')

                cmd.stdin.write(batch)
                cmd.stdin.flush()
                # result = cmd.stdout.read()
                # print(result.decode())

                processing = 1

                while processing:
                    time.sleep(2)
                    new_cont = os.listdir(dir_new)

                    if set_file[:-1] + '.clu.' + str(tetrode) in new_cont:
                        processing = 0
                        try:
                            os.rename(clu_name, cut_path)
                        except PermissionError:
                            processing = 1
        cur_time = datetime.datetime.now().time()
        fin_msg = ': Analysis in this directory has been completed!'
        print(str(cur_time)[:8] + fin_msg)
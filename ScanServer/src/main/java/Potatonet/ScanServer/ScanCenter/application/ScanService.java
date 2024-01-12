package Potatonet.ScanServer.ScanCenter.application;

import Potatonet.ScanServer.ScanCenter.dao.IpRepository;
import Potatonet.ScanServer.ScanCenter.domain.DataPair;
import Potatonet.ScanServer.ScanCenter.domain.Ip;
import ch.qos.logback.core.joran.sanity.Pair;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import static Potatonet.ScanServer.Global.Config.scanConfig.*;

@Service
public class ScanService {

    @Autowired
    IpRepository ipRepository;
    List<Integer> portList = new ArrayList<>();

    Long current_idx = 0l;


    public void setPortList(List<Integer> newPortList){
        portList = newPortList;
    }

    public DataPair getPartOfIpWithPort(){
        List<Ip> IPs = getPartOfIp();

        return new DataPair(IPs,portList);
    }

    public List<Ip> getPartOfIp(){
        List<Ip> returnIps= ipRepository.findByipIdBetween(current_idx,current_idx+scanReturn);
        current_idx+=scanReturn;


        if(current_idx>ipRepository.findMaxIpId()){
            current_idx=0l;
        }
        return returnIps;
    }
}

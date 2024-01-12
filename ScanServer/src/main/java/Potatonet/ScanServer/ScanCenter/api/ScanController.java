package Potatonet.ScanServer.ScanCenter.api;

import Potatonet.ScanServer.ScanCenter.application.ScanService;
import Potatonet.ScanServer.ScanCenter.domain.DataPair;
import Potatonet.ScanServer.ScanCenter.domain.Ip;
import java.util.List;
import java.util.Map;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.antlr.v4.runtime.misc.Pair;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@Slf4j
@Controller
@RequiredArgsConstructor
public class ScanController {
    private final Ip ip;

    @Autowired
    ScanService scanService;

    @GetMapping("/partscan")
    public ResponseEntity<DataPair> distributePart(){
        DataPair listOfPart = scanService.getPartOfIpWithPort();
        return ResponseEntity.ok(listOfPart);
    }

    @PostMapping("/setPort")
    public ResponseEntity<String> portSetter(@RequestBody List<Integer> portList){
        scanService.setPortList(portList);
        return ResponseEntity.ok("SUCCESS");
    }

}

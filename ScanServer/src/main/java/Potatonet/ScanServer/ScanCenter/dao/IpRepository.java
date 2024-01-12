package Potatonet.ScanServer.ScanCenter.dao;

import Potatonet.ScanServer.ScanCenter.domain.Ip;
import java.util.List;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

@Repository
public interface IpRepository extends JpaRepository<Ip,String> {
    List<Ip> findByipIdBetween(Long startId, Long endId);

    @Query("SELECT MAX(e.ipId) FROM Ip e")
    Long findMaxIpId();

}
